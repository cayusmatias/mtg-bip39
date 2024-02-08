# Magic BIP-39 Mapper (English)

## Description

Magic BIP-39 Mapper is a project that bridges the world of Magic: The Gathering (MTG) and cryptocurrency security using the BIP-39 list. Through an innovative method, the project associates words from the BIP-39 list, used to generate bitcoin wallet seeds, with specific MTG cards. This mapping is carried out using eight specific MTG collections, each containing at least 256 cards, allowing a direct correspondence between each word from the BIP-39 list and a unique card within these collections.

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

### BIP39 Mnemonic to Magic: The Gathering Card Mapping Logic

This application maps BIP39 mnemonic words to Magic: The Gathering (MTG) cards using a unique logic based on set codes and card indices. Here's an overview of how the mapping process works:

- **BIP39 Words**: The BIP39 standard includes a list of 2048 unique words used in the generation of cryptocurrency wallet seed phrases.

- **MTG Sets**: The application requires a selection of 8 distinct MTG set codes. Each set should contain at least 256 unique cards to ensure a broad mapping range. This selection is crucial because it divides the 2048 BIP39 words evenly across the sets, with each set representing a segment of 256 words.

- **Mapping Logic**: 
    - The total number of BIP39 words (2048) is divided by the number of chosen MTG sets (8), resulting in 256. This means each MTG set is responsible for representing a subset of 256 BIP39 words.
    - A word's index within the BIP39 list determines its mapped card. The index is used alongside a set's position in the `SET_CODES` list to calculate the specific card within that set.
    - The offset for each set is determined by its position in the `SET_CODES` list, multiplied by 256. For example, the first set in the list maps to words 0-255, the second set to words 256-511, and so on.

- **User Customization**:
    - Users can customize the `SET_CODES` list by changing the order of the sets or selecting different sets. However, it's essential to note that any changes to the set selection or order will alter the mapping.
    - To decode a mnemonic correctly back to words, users must know the original `SET_CODES` configuration used to encode the mnemonic.

### Important Note:
The order of the sets in `SET_CODES` is critical to the mapping logic. A different order or set selection generates a different card mapping for the same BIP39 word. Users are advised to keep track of their `SET_CODES` configuration for consistent encoding and decoding of mnemonics.

```python
# Example of a default SET_CODES configuration in config.py
SET_CODES = ['mkm', 'lci', 'woe', 'mom', 'one', 'bro', 'dmu', 'snc']
```

## Usage

This section guides you through getting the application up and running on your local machine. There are two ways to run the application: directly using Python Flask or within a Docker container.

### Running with Python Flask

1. **Clone the Repository**

Clone the repository to your local machine using Git:

```bash
git clone https://github.com/cayusmatias/mtg-bip39.git
cd mtg-bip39
```

Set Up a Virtual Environment

Create a virtual environment for the project (if you don't have virtualenv installed, you can install it using pip):
```bash
pip install virtualenv
virtualenv venv

# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

Install Dependencies

Install all required dependencies with:
```bash
pip install -r requirements.txt
```

Start the application with Flask:
```bash
flask run
```

Running with Docker

You can start the application with Docker Compose:

```bash
docker-compose up --build
```

## Upcoming Features

In our commitment to continuously improve and secure our application, we are excited to share the roadmap for upcoming features. These enhancements are designed to provide a more robust, efficient, and secure experience for our users:

### Local Database Population

- **SQLite3 Database Integration**: We plan to introduce the capability to populate a local SQLite3 database with the set data configured in `config.py`. This feature aims to streamline the process of managing and accessing MTG card data within the application, reducing dependencies on external APIs for data retrieval.

### Local Card Data Storage

- **Downloading Cards to Static Folder**: To further enhance data privacy and application performance, we will implement functionality to download card images and details directly into the application's `static` folder. This move towards exclusively local data storage minimizes the security risks associated with external API calls and ensures that card data is readily available for faster access and display.

### Security and Performance Enhancements

- **Minimizing API Dependency**: By storing card data locally, we significantly reduce the number of calls made to the Scryfall API, decreasing potential exposure to security vulnerabilities and enhancing overall application performance.
- **Local Data Management**: Users will gain greater control over their data, with the ability to manage and update their local card database as new sets are released or as their needs change.

### Downloadable PDF for Printing Proxies

- **Real-Size Card PDFs**: A significant addition to our suite of features will be the capability for users to download a PDF containing the cards in real size. This will allow enthusiasts to print out proxy cards for Magic: The Gathering and store them in a physical deck if they don't have the original card.

### Looking Ahead

These features are part of our broader vision to make the application self-sufficient and secure. We understand the importance of data privacy and are dedicated to providing solutions that respect user autonomy while delivering the rich functionality that our community values.

Stay tuned for updates as we progress in implementing these exciting features. Your feedback and suggestions are always welcome as we strive to make this application better for everyone.


## Credits

If you use this project or learn from it to develop your own project, please give credit by mentioning my name and linking to the original repository. We appreciate recognition for the work contributed to the open-source community.

## License

[MIT](https://choosealicense.com/licenses/mit/)
