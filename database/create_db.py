import sqlite3

# Script to create parent and child table for NFL related twitter data. Will follow same structor for other sports

connection = sqlite3.connect('slant.db')

cursor = connection.cursor()

# parent table for the NFL
cursor.execute("""
    CREATE TABLE IF NOT EXISTS nfl_teams (
        id INTEGER PRIMARY KEY,
        team TEXT NOT NULL UNIQUE
    )
""")

# parent table for the NBA
cursor.execute("""
    CREATE TABLE IF NOT EXISTS nba_teams (
        id INTEGER PRIMARY KEY,
        team TEXT NOT NULL UNIQUE
    )
""")

# parent table for the NBL
cursor.execute("""
    CREATE TABLE IF NOT EXISTS nbl_teams (
        id INTEGER PRIMARY KEY,
        team TEXT NOT NULL UNIQUE
    )
""")

# parent table for the NHL
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

# posts table will store all of the data that is pulled from a tweet as well as the sentiment data that is determined.
# As requests are made for information on a date range from A to B, the text from posts in that range will be pulled and
# fed into the cosine-sim to idenfify the keyphrases which will be returned to user alongside sentiment data.
# Dynamically evaluating the posts for keyphrases rather than attempting to separate them prior to databasing is
# redundant and therefor inefficient. This also keeps the database structure more simple, putting less stress on the system
# handing the database when large requests are made.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        team_id INTEGER NOT NULL,
        user NOT NULL,
        body TEXT NOT NULL,
        positive NOT NULL,
        neutral NOT NULL
        negative NOT NULL,
        compound NOT NULL,
        likes INTEGER NOT NULL,
        shares INTEGER NOT NULL,
        date NOT NULL,
        FOREIGN KEY (team_id) REFERENCES nfl_teams (id)
    )
""")

# Storing phrases as individual items is inefficient. Every time a call is made to the database to evaluate a particular date range, 
# the evaluation of the phrases will need to be done dynamically as the dataset is constantly changing and result will vary.
# It is faster to store just the raw text and sentiment data inside the 'posts' table and to process phrases on-call.
# Keeping this here as a reference incase things change.
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS phrases (
#         id INTEGER PRIMARY KEY,
#         team_id INTEGER NOT NULL,
#         post_id INTEGER NOT NULL,
#         body TEXT NOT NULL,
#         date NOT NULL,
#         FOREIGN KEY (post_id) REFERENCES posts (id),
#         FOREIGN KEY (team_id) REFERENCES nfl_teams (id)
#     )
# """)

# hashtags table will be used to store the official hashtags of the associated team.
# Currently avoiding including the unofficial hashtags as those seem to be heavily associated with unrelated posts.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS hashtags (
        id INTEGER PRIMARY KEY,
        team_id INTEGER NOT NULL,
        tag TEXT NOT NULL,
        FOREIGN KEY (team_id) REFERENCES nfl_teams (id)
    )
""")

connection.commit()
