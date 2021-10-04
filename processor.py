# Nearly complete module for sentiment analysis of a text. Only changes that are needed currently are to tweak sensitivity. 

from itertools import count
import pandas as pd
import numpy as np
from nltk.tokenize import RegexpTokenizer #to tokenize the text body
from nltk.corpus import stopwords #to remove stopwords that do not add value to the analysis
from nltk.stem import WordNetLemmatizer #to simplify words into more basic forms
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from nltk.stem import PorterStemmer
from nltk import FreqDist
import emoji
import re #to remove links that may be in the text body
import spacy

# Class that contains methods for cleaning input data to prepare for sentiment analysis
class PreProcess:

    def __init__(self) -> None:
        pass

    # Method that removes any emojies identified inside the textbody to help feed more clean data into NLP.
    def removeEmoji(self, textBody):
        string_emojiless = emoji.get_emoji_regexp().sub(u'', textBody) #removes all instances of emojis from textbody
        
        return string_emojiless #returns string
    
    # Method that will tokenize the text body and return the contents in a list form.
    # More effective and efficient that splitting the string.
    def tokenizeString(self, emojiless_textbody):
        tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|http\S+')

        tokenized_string = tokenizer.tokenize(emojiless_textbody) #tokenizes textbody into a list
        
        return tokenized_string #returns list of words

    # Method that iterates through the list-form text, converts all values to lowercase, and return in a list form
    def makeLowerCase(self, tked_list):
        text_lowcase = []

        for word in tked_list: #iterates through tk text and makes all words lowercase
            text_lowcase.append(word.lower())

        return text_lowcase #returns list

    # Method removes all identified stopwords from the textlist to further clean the data before NLP.
    # Stop words do not provide any information to the analysis.
    def removeStopWords(self, LC_list):
        nlp = spacy.load('en_core_web_sm') #retrieving english data from spacy
        stopwords = nlp.Defaults.stop_words #getting known stopwords from enlish data

        text_NoSW = []

        for word in LC_list: #parsing and removing stopwords from list
            if word not in stopwords:
                text_NoSW.append(word)

        return text_NoSW #returns list

    # Method lemmatizes words, putting them in a more basic and comprehensible format for NLP.
    def lemmatizer(self, word_list):
        lemmatizer = WordNetLemmatizer() #creating lemmatizer object

        lemmatized_tks = []

        for word in word_list: #iterating through word list and lemmatizing
            lemmatized_tks.append(lemmatizer.lemmatize(word))

        return lemmatized_tks #returns list
        
# Class that apply preprocessing methods and then analyzes the resulting text.
# Will output -1 or 1 at completion of process representing negative or positive sentiment
class Analyze:

    def __init__(self) -> None:
        pass

    # Method that calls all preProcessing methods at once and returns a simplified list of strings.
    def preProcess(self, text):
        prep = PreProcess()

        stepOne = prep.removeEmoji(text)
        stepTwo = prep.tokenizeString(stepOne)
        stepThree = prep.makeLowerCase(stepTwo)
        stepFour = prep.removeStopWords(stepThree)
        result = prep.lemmatizer(stepFour)

        return result #returns list

    # Method uses NLTK's VADER method for evaluating the polarity of each word from the cleaned input.
    # Returns an organized DataFrame containing each word and it's assigned polarity.
    # Any word with a polarity outside the (-0.10, 0.10) interval will be assigned -1 and 1 respectively.
    # All words inside that interval are assigned a neutral value.
    def sentiment(self, cleaned_text):
        sia = SIA()
        results = []

        for phrases in cleaned_text: #apply VADER word by word
            pol_score = sia.polarity_scores(phrases)
            pol_score['words'] = phrases #saving the determined polarity to a dictionary
            results.append(pol_score) #adding resulting k:v pair to list

        pd.set_option('display.max_columns', None, 'max_colwidth', None)
        df = pd.DataFrame.from_records(results) #converting the results list into a dataframe
        df['label'] = 0 #adding a label column to simplify reading
        df.loc[df['compound'] > 0.10, 'label'] = 1 #adding label positive
        df.loc[df['compound'] < -0.10, 'label'] = -1 #adding label negative
        
        return df #returns dataframe

    # Method that evaluates the dataframe to determine the sentiment skew.
    # Returns a -1 or 1 for Negative or Positive skew respectively.
    def findSkew(self, data_df): 
        data_PosNeg = data_df.loc[data_df['label'] != 0] #filtering out words with neutral labels.
        count = data_PosNeg.label.value_counts().idxmax() #determining value with highest occurrence

        return count



