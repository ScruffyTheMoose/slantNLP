import sqlite3

# Script to create parent and child table for NFL related twitter data. Will follow same structor for other sports

connection = sqlite3.connect('nfl.db')

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS nfl_teams (
        id INTEGER PRIMARY KEY,
        team TEXT NOT NULL UNIQUE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS nba_teams (
        id INTEGER PRIMARY KEY,
        team TEXT NOT NULL UNIQUE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS nbl_teams (
        id INTEGER PRIMARY KEY,
        team TEXT NOT NULL UNIQUE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS nhl_teams (
        id INTEGER PRIMARY KEY,
        team TEXT NOT NULL UNIQUE
    )
""")

# FIFA (and all football) is tbd since it is massive and will require a ton of work to buildup to resources to handle
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS fifa_teams (
#         id INTEGER PRIMARY KEY,
#         team TEXT NOT NULL UNIQUE
#     )
# """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        team_id INTEGER NOT NULL,
        sentiment NOT NULL,
        likes INTEGER NOT NULL,
        shares INTEGER NOT NULL,
        date NOT NULL,
        FOREIGN KEY (team_id) REFERENCES nfl_teams (id)
    )
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS phrases (
        id INTEGER PRIMARY KEY,
        team_id INTEGER NOT NULL,
        post_id INTEGER NOT NULL,
        body TEXT NOT NULL,
        date NOT NULL,
        FOREIGN KEY (post_id) REFERENCES posts (id),
        FOREIGN KEY (team_id) REFERENCES nfl_teams (id)
    )
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS hashtags (
        id INTEGER PRIMARY KEY,
        team_id INTEGER NOT NULL,
        tag TEXT NOT NULL,
        FOREIGN KEY (team_id) REFERENCES nfl_teams (id)
    )
""")

connection.commit()
