# I am leaving this as a placeholder for the updated version for sentiment data.
# This is (obviously) not a database for sentiment related data. This is from a separate finance related algorithm.
# Please look at the 'processor' module to see what data will be gathered, analyzed, and it's dataframe output.

import sqlite3

connection = sqlite3.connect('app.db')

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock (
        id INTEGER PRIMARY KEY,
        symbol TEXT NOT NULL UNIQUE,
        company TEXT NOT NULL UNIQUE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_price (
        id INTEGER PRIMARY KEY,
        stock_id INTEGER,
        date NOT NULL,
        open NOT NULL,
        high NOT NULL,
        low NOT NULL,
        close NOT NULL,
        adjusted_close NOT NULL,
        volume NOT NULL,
        FOREIGN KEY (stock_id) REFERENCES stock (id)
    )
""")

connection.commit()
