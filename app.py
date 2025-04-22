from flask import Flask, render_template, render_template_string, request
from config import SET_CODES, ENV
from scryfall_api import *
import time

app = Flask(__name__)


@app.context_processor
def inject_env():
    return dict(ENV=ENV)


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
    mtg_cards_list = []
    mtg_cards_imgs = []
    
    for i, word in enumerate(bip39_words.split(), 1):
        time.sleep(0.05)
        set_code, card_number = find_card_by_word(word, SET_CODES)
        if set_code and card_number:
            card_info = get_card_from_set(set_code, card_number)
            if card_info:
                card_name, set_code, card_number = card_info['name'], set_code, card_number
                mtg_cards_list.append(f"<li>{i} - {card_name} <{str(card_number).zfill(3)}> [{set_code}]</li>")
                
                # Get the appropriate image URL
                if 'card_faces' in card_info and 'image_uris' in card_info['card_faces'][0]:
                    img_url = card_info['card_faces'][0]['image_uris']['normal']
                else:
                    img_url = card_info['image_uris']['normal']
                
                # Add the card image details to the list
                mtg_cards_imgs.append({
                    'src': img_url,
                    'alt': card_name,
                    'index': i
                })
    
    conversion_result = ''.join(mtg_cards_list)
    
    return render_template('card_results.html', 
                          conversion_result=conversion_result, 
                          mtg_cards_imgs=mtg_cards_imgs)


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


@app.route('/download-image')
def download_image():
    url = request.args.get('url')
    filename = request.args.get('filename', 'mtg-card')
    
    if not url:
        return "URL parameter is required", 400
    
    try:
        # Use requests to fetch the image
        import requests
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Create a response with the image data
        from flask import send_file, Response
        from io import BytesIO
        
        return Response(
            response.iter_content(chunk_size=1024),
            headers={
                'Content-Disposition': f'attachment; filename="{filename}.jpg"',
                'Content-Type': response.headers.get('Content-Type', 'image/jpeg')
            }
        )
    except Exception as e:
        return f"Error downloading image: {str(e)}", 500


if __name__ == '__main__':
    if ENV == 'prod':
        app.run(host='0.0.0.0', port=5000)
    else:
        app.run(debug=True)