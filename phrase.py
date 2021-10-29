from processor import Sentiment as sn


# Class Phrase will be used to track data specific to each individual phrase pulled out of a Post object.
class Phrase:

    def __init__(self, baseText, team, datetime):
        self.pos = sn.sentiment(baseText)['pos']
        self.nue = sn.sentiment(baseText)['neu']
        self.neg = sn.sentiment(baseText)['neg']
        self.compound = sn.sentiment(baseText)['compound']

        self.team = team

        self.datetime = datetime
