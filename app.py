from flask import Flask, render_template, render_template_string, request
from config import SET_CODES
from scryfall_api import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/bip2mtg')
def bip2mtg():
    return render_template('bip2mtg.html')


@app.route('/mtg2bip')
def mtg2bip():
    return render_template('mtg2bip.html')


@app.route('/convert-bip2mtg', methods=['POST'])
def convert_bip2mtg():
    bip39_words = request.form['bip39Words'].lower()
    mtg_cards = ''
    mtg_cards_imgs = ''
    for word in bip39_words.split():
        set_code, card_number = find_card_by_word(word, SET_CODES)
        if set_code and card_number:
            card_info = get_card_from_set(set_code, card_number)
            if card_info:
                card_name, set_code, card_number = card_info['name'], set_code, card_number
                mtg_cards += f"<li>{card_name} <{str(card_number).zfill(3)}> [{set_code}]</li>"
                mtg_cards_imgs += f"<img class='zoom-hover rounded-3' src='{card_info['image_uris']['normal']}' alt='{card_name}'>"
                     
    conversion_result = mtg_cards
    
    return render_template_string("""<div class='row mb-4'>
                                        <div class='col-md-4'>
                                            <h3 class='text-secondary'>Cards List</h3>
                                            <ol>{{ conversion_result|safe }}</ol>
                                        </div>
                                        <div class='col-md-8'>
                                            <h3 class='text-secondary'>Cards Images</h3>{{ mtg_cards_imgs|safe }}
                                        </div>
                                     </div>""", 
                                  conversion_result=conversion_result, mtg_cards_imgs=mtg_cards_imgs)


@app.route('/convert-mtg2bip', methods=['POST'])
def convert_mtg2bip():
    cards = request.data.decode('utf-8').split()
    mnemonic = ''
    for index, card in enumerate(cards):
        card = card.zfill(6).lower()
        try:
            card_number = int(card[0:3])
            #check if card number is 1 to 256
            if card_number < 1 or card_number > 256:
                return f"Invalid card number: '{card_number}' in card {index + 1}"
        except ValueError:
            return f"Invalid card number: '{card[0:3]}' in card {index + 1}"
        
        set_code = card[3:]
        
        # verify if set_code is valid
        if set_code in SET_CODES:
            word = map_card_to_word(SET_CODES, set_code, card_number)
            if word:
                mnemonic += bip39_words[word - 1] + ' '
        else:
            return f"Invalid set code: '{set_code}' in card {index + 1}"

    return mnemonic


if __name__ == '__main__':
    app.run(debug=True)