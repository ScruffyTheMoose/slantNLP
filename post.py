from processor import PreProcess as pp
from processor import Sentiment as sn
from processor import Keywords as kw

# This module will be used to create Post object representing a single tweet. 
# They will contain the initial information: tweet text, date/time, user, likes, shares, etc. when instantiated.
# The Post object will also apply the processor pipeline and store resulting data.
# It will be much easier to then feed each Post object into the populate_db module.

class Post:

    # Constructor
    def __init__(self, user, baseText, datetime, likes, shares):
        self.user = user
        self.baseText = baseText
        self.datetime = datetime
        self.likes = likes
        self.shares = shares

        self.cleanText = pp.run(baseText)

        self.pos = sn.sentiment(baseText)['pos']
        self.neu = sn.sentiment(baseText)['neu']
        self.neg = sn.sentiment(baseText)['neg']
        self.compound = sn.sentiment(baseText)['compound']

        self.keyPhrases = kw.keyphrases(baseText)
