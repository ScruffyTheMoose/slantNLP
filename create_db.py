# Please look at the 'processor' module to see what data will be gathered, analyzed, and it's dataframe output.

import sqlite3

# Script to create parent and child table for NFL related twitter data. Subject to change given different data related needs.

connection = sqlite3.connect('nfl.db')

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS nfl_teams (
        id INTEGER PRIMARY KEY,
        tag TEXT NOT NULL UNIQUE,
        team TEXT NOT NULL UNIQUE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_price (
        id INTEGER PRIMARY KEY,
        team_id INTEGER,
        body TEXT NOT NULL,
        sentiment NOT NULL,
        tags NOT NULL,
        keywords,
        likes INTEGER,
        date NOT NULL,
        FOREIGN KEY (team_id) REFERENCES nfl_teams (id)
    )
""")

connection.commit()
