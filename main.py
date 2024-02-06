import requests
from bip39_words import bip39_words

def get_card_from_set(set_code, card_number):
    """Busca uma carta específica de um conjunto na API do Scryfall."""
    url = f"https://api.scryfall.com/cards/{set_code}/{card_number}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def map_card_to_word(set_codes, set_code, card_number):
    """Mapeia o número da carta para a palavra BIP-39 com base no conjunto."""
    total_words = 2048
    offset_multiplier = 256  # Cada conjunto tem um offset de 256 palavras.
    
    # Encontra o índice do conjunto e calcula o offset.
    set_index = set_codes.index(set_code)
    offset = set_index * offset_multiplier
    
    # Calcula o número da palavra na lista BIP-39.
    word_number = offset + card_number
    if word_number > total_words:
        return None  # Retorna None se o número exceder o total de palavras BIP-39.
    
    return word_number


def find_word_index(word):
    """Encontra o índice de uma palavra na lista BIP-39."""
    try:
        return bip39_words.index(word) + 1  # Adiciona 1 porque a lista começa em 0
    except ValueError:
        return None


def find_card_by_word(word, set_codes):
    """Determina o conjunto e o número da carta com base na palavra BIP-39."""
    word_index = find_word_index(word)
    if word_index is None:
        return None, None  # Palavra não encontrada
    
    offset_multiplier = 256
    set_index = (word_index - 1) // offset_multiplier  # Determina o índice do conjunto
    if set_index >= len(set_codes):
        return None, None  # Índice fora do alcance dos conjuntos disponíveis
    
    set_code = set_codes[set_index]
    card_number = (word_index - 1) % offset_multiplier + 1  # Calcula o número da carta dentro do conjunto
    
    return set_code, card_number


# Exemplo de uso
set_codes = ['mkm', 'lci', 'woe', 'mom', 'one', 'bro', 'dmu', 'snc']  # Substitua por códigos reais dos conjuntos.
set_code = 'woe'  # Código do conjunto que você quer consultar.
card_number = 151  # Número da carta no conjunto.

# Obtem a carta específica
card_info = get_card_from_set(set_code, card_number)
print(card_info.get('name'))
print(card_info.get('image_uris').get('normal'))

# Mapeia a carta para a palavra BIP-39
word_index = map_card_to_word(set_codes, set_code, card_number)
if word_index:
    print(f"A carta {card_number} do conjunto {set_code} mapeia para a palavra número {word_index} da lista BIP-39.")
else:
    print("Número da palavra inválido ou fora do alcance.")

# Encontra a carta com base na palavra BIP-39
word = "fan"  # Palavra que você quer encontrar
set_code, card_number = find_card_by_word(word, set_codes)

if set_code and card_number:
    print(f"A palavra '{word}' corresponde à carta número {card_number} do conjunto {set_code}.")
else:
    print("Palavra não encontrada ou fora do alcance dos conjuntos definidos.")
