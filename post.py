import string
from processor import Sentiment as sn
import datetime

# This module will be used to create Post object representing a single tweet. 
# They will contain the initial information: tweet text, date/time, user, likes, shares, etc. when instantiated.
# The Post object will also apply the processor pipeline and store resulting data.
# It will be much easier to then feed each Post object into the populate_db module.

class Post:

    # Constructor which assigned data from parameters and then applies those arguments to components from processor module
    def __init__(self, user: string, team: string, baseText: string, datetime: datetime, likes: int, shares: int) -> None:
        
        # storing basic data for the post that will be fed directly into the database
        self.user = user
        self.team = team
        self.baseText = baseText
        self.likes = likes
        self.shares = shares
        self.datetime = datetime


    # Method to assign instance variables containing sentiment information to each post.
    def setSentiment(self) -> None:
        sentiment = sn.sentiment(self.baseText)

        self.positive = sentiment['pos']
        self.neutral = sentiment['neu']
        self.negative = sentiment['neg']
        self.compound = sentiment['compound']
