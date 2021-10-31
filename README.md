

slantNLP is a tool that will allow a user to evaluate the sentiment towards any US based sports team through Twitter. This process is achieved through a multi-step process of searching, parsing, analyzing, databasing, and presenting.

This program is still under construction! I am learning a lot as I piece it together and I appreciate you taking a look.



--





**Searching** - 
Using Tweepy, we access the Twitter API and make calls seaching for a particular set of #hashtags relating to the target team. The Tweets that match our search are pulled in for evaluation.

**Parsing** - 
Once a Tweet gets pulled in, we parse through the data pulling out important information like _user, related team, text, date, likes, and retweets_. 

**Analyzing** -
The parsed data gets fed into a Natural Language Processing pipeline powered by NLTK, spaCy, and sci-kit learn. 

NLTK and spaCy are used to clean the text-body of the Tweet so as to prevent any unusual symbols or stopwords from being analyzed as well as splitting the text-body into phrases. The cleaned phrases are then fed into a VADER model for Twitter which will evaluate and return a sentiment score for each phrase. The phrases are then aggregated into a database table linked to the respective team.

Once the phrases are evaluated and databased, sklearn is used to determine if there are any phrases that are representative of the sentiment of a significant portion of the sample population - _specPhrases_. If the determination is yes, sklearn will find those phrases and store them as representative of a sample of Tweets.

**Databasing** -
Elements from each step in this process are gradually being added to a large, linked database of different data components. Tables consisting of _teams_ identified by sport as well as tables for _posts, phrases, specPhrases, hashtags_ which are all interconnected to keep track of the associated _user, team, date, _and_ sentiment_.

**Presenting** -
Once all data has been processed and stored, it needs to be presented in a clean and efficient manner to the end-user. The construction and functionality of this is still TBD, but is planned to be through a web framework (likely flask) that makes calls to the DB and presents a sentiment breakdown for the desired period of time/team as well as the _specPhrases_.
