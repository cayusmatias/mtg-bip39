import requests
from bip39_words import bip39_words
from config import SET_CODES


def get_card_from_set(set_code, card_number):
    """Fetches a specific card from a set using the Scryfall API."""
    url = f"https://api.scryfall.com/cards/{set_code}/{card_number}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def map_card_to_word(set_codes, set_code, card_number):
    """Maps the card number to a BIP-39 word based on the set."""
    total_words = 2048
    offset_multiplier = 256  # Each set has an offset of 256 words.
    
    # Finds the set index and calculates the offset.
    set_index = set_codes.index(set_code)
    offset = set_index * offset_multiplier
    
    # Calculates the word number in the BIP-39 list.
    word_number = offset + card_number
    if word_number > total_words:
        return None  # Returns None if the word number exceeds the total BIP-39 words.
    
    return word_number


def find_word_index(word):
    """Finds the index of a word in the BIP-39 list."""
    try:
        return bip39_words.index(word) + 1  # Adds 1 because the list starts at 0
    except ValueError:
        return None


def find_card_by_word(word, set_codes):
    """Determines the set and card number based on a BIP-39 word."""
    word_index = find_word_index(word)
    if word_index is None:
        return None, None  # Word not found
    
    offset_multiplier = 256
    set_index = (word_index - 1) // offset_multiplier  # Determines the set index
    if set_index >= len(set_codes):
        return None, None  # Index out of range of available sets
    
    set_code = set_codes[set_index]
    card_number = (word_index - 1) % offset_multiplier + 1  # Calculates the card number within the set
    
    return set_code, card_number
