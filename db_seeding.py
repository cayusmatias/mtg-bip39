import sqlite3

# Create a connection to the database
conn = sqlite3.connect('cards.db')

# Create a cursor
cursor = conn.cursor()

# Create a table cards if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cards (
        id INTEGER PRIMARY KEY,
        set_code TEXT,
        set_name TEXT,
        card_number INTEGER,
        name TEXT,
        image_uri TEXT,
        image_path TEXT
    )
''')