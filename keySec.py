import json


# Class that will read/add keys from/to a text file (dict) for the twitter API for OAuth 2
class twitterKeys:

    # Method can be used to generate a new text file with keys inside a specific directory
    def createFile(filename, bearer, apiKey, apiSecret):

        # validating proper filetype in chosen name
        if filename[-4:] != ".txt":
            filename = filename + ".txt"

        details = { 
                    'bearer': bearer, 
                    'apiKey': apiKey, 
                    'apiSecret':apiSecret
                    }
        
        # writing information to file
        with open(filename, 'w') as convert_file:
            convert_file.write(json.dumps(details))

    # Method to read keys from file
    def readFile(filename):

        if filename[-4:] != ".txt":
            filename = filename + ".txt"

        # user will need to specificy directory to read from in this line.
        filename = "/home/scruffy/Documents/Python/slantNLP/" + filename

        with open(filename) as f:
            data = f.read()

        out = json.loads(data)

        return out
