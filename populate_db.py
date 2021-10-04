# Leaving this as a placeholder for a modified version specifically for sentiment related data.
# This is from a finance related algorithm I am building that is sending data to a SQLite db.

import sqlite3
import json
from urllib.request import urlopen

url = "https://financialmodelingprep.com/api/v3/stock/list?apikey=*****"

def getParsedData(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

# symbols are located at each index under key "symbol" -> rawData[0]["symbol"]
# company names are located under similar index and key -> rawData[0]["name"]
rawData = getParsedData(url)

# print(rawData[0])
#==========================================

connection = sqlite3.connect('app.db')

cursor = connection.cursor()

ec = 0

for i in range(0, len(rawData)-1):
    tSymbol = rawData[i]["symbol"]
    tCompany = rawData[i]["name"]

    if "'" in tCompany:
        tCompany = tCompany.replace("'", "")


    if "." not in rawData[i]["symbol"]:
        try:
            cursor.execute("INSERT INTO stock (symbol, company) VALUES ('{}', '{}')".format(tSymbol, tCompany))
        except Exception as e:
            ec += 1
            print(ec)
            print(rawData[i]["symbol"])
            print(e)
    else:
        continue

connection.commit()
