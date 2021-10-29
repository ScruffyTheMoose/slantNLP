from nltk.tokenize import RegexpTokenizer #to tokenize the text body
from nltk.stem import WordNetLemmatizer #to simplify words into more basic forms
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import emoji
import re #to remove links that may be in the text body
import spacy
from string import punctuation

# Class that contains methods for cleaning input data to prepare for sentiment analysis
class PreProcess:

    def __init__(self) -> None:
        pass

    # Method that removes any emojies identified inside the textbody to help feed more clean data into NLP.
    def removeEmoji(textBody):
        string_emojiless = emoji.get_emoji_regexp().sub(u'', textBody) #removes all instances of emojis from textbody
        
        return string_emojiless #returns string
    
    # Method that will tokenize the text body and return the contents in a list form.
    # More effective and efficient that splitting the string.
    def tokenizeString(emojiless_textbody):
        tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|http\S+')

        tokenized_string = tokenizer.tokenize(emojiless_textbody) #tokenizes textbody into a list
        
        return tokenized_string #returns list of words

    # Method that iterates through the list-form text, converts all values to lowercase, and return in a list form
    def makeLowerCase(tked_list):
        text_lowcase = []

        for word in tked_list: #iterates through tk text and makes all words lowercase
            text_lowcase.append(word.lower())

        return text_lowcase #returns list

    # Method removes all identified stopwords from the textlist to further clean the data before NLP.
    # Stop words do not provide any information to the analysis.
    def removeStopWords(LC_list):
        nlp = spacy.load('en_core_web_sm') #retrieving english data from spacy
        stopwords = nlp.Defaults.stop_words #getting known stopwords from enlish data

        text_NoSW = []

        for word in LC_list: #parsing and removing stopwords from list
            if word not in stopwords:
                text_NoSW.append(word)

        return text_NoSW #returns list

    # Method lemmatizes words, putting them in a more basic and comprehensible format for NLP.
    def lemmatizer(word_list):
        lemmatizer = WordNetLemmatizer() #creating lemmatizer object

        lemmatized_tks = []

        for word in word_list: #iterating through word list and lemmatizing
            lemmatized_tks.append(lemmatizer.lemmatize(word))

        return lemmatized_tks #returns list

    # Method that will operate all preceding code blocks in sequence
    # Returns list of lemmatized words from input text
    def run(text):
        stage1 = PreProcess.removeEmoji(text)
        stage2 = PreProcess.tokenizeString(stage1)
        stage3 = PreProcess.makeLowerCase(stage2)
        stage4 = PreProcess.removeStopWords(stage3)
        return PreProcess.lemmatizer(stage4)
        
# Class that apply preprocessing methods and then analyzes the resulting text for sentiment.
# Will output -1 or 1 at completion of process representing negative or positive sentiment
class Sentiment:

    def __init__(self) -> None:
        pass

    # Method uses the VADER SentimentInstensityAnalyzer to evaluate the sentiment of the base text without cleaning.
    # This gives the tool full access to the population of words rather than a cleaned text so that it may more accurately evaluate sentiment.
    # VADER score (vs) is then evaluated for thresholds and returns result. This needs tweaking.
    # Significantly faster than previous methods.
    def sentiment(text):
        analyzer = SentimentIntensityAnalyzer()
        vs = analyzer.polarity_scores(text)

        return vs

# Class that evaluates the keywords and keyphrases in the text being evaluated.
# These phrases will be used to identify shared sentiment across a large number of posts.
# Opted to use scispaCy pipeline since it is apparently more effective at identifying keywords in the target material.
class Keywords:

    def __init__(self) -> None:
        pass

    # Method identifies keyphrases in text by simply splitting the text body by punctuation.
    # This is the most efficient way to break a text into English phrases without needed to rebuild sentences from ground up.
    # These will be stores and used to evaluate common sentiment across numerous texts.
    # This is also exponentially faster than previousl methods
    def keyphrases(text):
        return re.split("[?!,.:;]", PreProcess.removeEmoji(text).lower())
