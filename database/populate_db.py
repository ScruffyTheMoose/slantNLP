import pandas as pd
import sqlite3

# Script to read in a CSV file of official hashtags for all NFL teams to the database for parent table
# This will become a full module with callable methods in the near future, but this will do for setting up the foundations.

df = pd.read_csv("nfl_teams.csv")

connection = sqlite3.connect('nfl.db')

cursor = connection.cursor()

for row in df.values:

    tag = row[0]
    team = row[1]

    cursor.execute("""
    INSERT INTO nfl_teams (tag, team) VALUES ('{}', '{}')
    """.format(tag, team))

connection.commit()
