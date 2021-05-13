import sys

import numpy
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import RegexpTokenizer
import numpy as np
numpy.set_printoptions(threshold=sys.maxsize)

def preprocess(_w):
    tokens = word_tokenize(_w)
    tokenizer = RegexpTokenizer(r"\w+")
    tokens = tokenizer.tokenize(listToString(tokens))
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    t = [lemmatizer.lemmatize(w) for w in tokens if not w in stop_words]
    return listToString(t)


def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ' ' + ele
        # return string
    return str1


def dictionary(doc):
    d = []
    for w in word_tokenize(doc):
        if not w in d:
            d.append(w)
    return d


def read_file():
    file = open("P_vs_NP.txt", "r")
    str = ""
    i = 0
    for line in file:
        str += line
    file.close()
    return str

def initialize(frequences, d):
    for w in d:
        frequences[w] = 0


doc = read_file()
d = dictionary(preprocess(doc))
print(d)
frequences = []
_doc = word_tokenize(doc)
#initialize(frequences, d)
matrix = np.zeros((len(d),len(_doc)))
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if (d[r] == _doc[c]):
            matrix[r][c] = 1
#print(matrix)
granularity = 100
matrix2 = np.zeros((len(d),int(len(_doc)/granularity)))
for r in range(len(matrix2)):
    for c in range(len(matrix2[r])):
        for i in range(granularity):
            matrix2[r][c] += matrix[r][i]
print(matrix2)