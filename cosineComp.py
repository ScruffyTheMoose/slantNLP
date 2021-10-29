from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import pairwise
import pandas as pd

# NEEDS DB TO OPERATE - must complete database compenent of phrases. This is dependant on pulling list of phrases to operate on.

# Uses Post object
# This module will iterate through the keyphrases of a data set to identify common phrases across the population.
# Will use sklearn cosin similarity to evaluate.

class Compare:

    def __init__(self) -> None:
        pass

    def createDocs(phraseList):
        None # to do

    def genMatrix(documents):
        n = len(documents)

        count_vectorizer = CountVectorizer(stop_words="english")

        sparse_matrix = count_vectorizer.fit_transform(documents)

        return pairwise.cosine_similarity(n, sparse_matrix)
