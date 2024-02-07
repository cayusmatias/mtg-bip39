# Magic BIP-39 Mapper (English)

## Description

Magic BIP-39 Mapper is a project that bridges the world of Magic: The Gathering (MTG) and cryptocurrency security using the BIP-39 list. Through an innovative method, the project associates words from the BIP-39 list, used to generate cryptocurrency wallet seeds, with specific MTG cards. This mapping is carried out using eight specific MTG collections, each containing at least 256 cards, allowing a direct correspondence between each word from the BIP-39 list and a unique card within these collections.

Each collection is assigned an "offset" based on its order position, with the first collection starting at 0 and each subsequent collection adding 256 to the offset. This method ensures that each card within a collection is associated with a specific word from the BIP-39 list, providing a unique and secure way to store your seed.

This project adopts a steganographic approach to hide and protect the BIP39 mnemonic phrase by embedding it within a curated selection of Magic: The Gathering cards. This technique not only secures the mnemonic from unauthorized discovery but also ensures it can be decoded exclusively by those familiar with the specific encoding strategy, offering a unique and secure way to manage cryptographic keys.

The collections used in this project are:

1. MKM (Murders at Karlov Manor)
2. LCI (The Lost Caverns of Ixalan)
3. WOE (Wilds of Eldraine)
4. MOM (March of the Machine)
5. ONE (Phyrexia: All Will Be One)
6. BRO (The Brothers' War)
7. DMU (Dominaria United)
8. SNC (Streets of New Capenna)

## Features

- Direct association of BIP-39 words with specific MTG cards through an offset system based on selected collections.
- Automatic search for card information and images via the Scryfall API.
- Support for all 2048 words from the BIP-39 list, using eight MTG collections with at least 256 cards each.

## Prerequisites

This project requires Python 3.x.

## Setup

...

## Usage

...

## Code Example

...

## Contributions

...

## Credits

If you use this project or learn from it to develop your own project, please give credit by mentioning my name and linking to the original repository. We appreciate recognition for the work contributed to the open-source community.

## License

[MIT](https://choosealicense.com/licenses/mit/)
