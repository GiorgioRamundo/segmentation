import collections
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
    stop_words.add('The')
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
        

def conta(w,l):
    f = 0
    for _w in word_tokenize(l):
        if w == _w:
            f = f + 1
    return f





_doc = read_file()
doc = preprocess(_doc)
d = dictionary(doc)
print(d)
print('found ' + str(len(d)) + ' words')
frequences = []
#_doc = word_tokenize(doc)
doc_lines = _doc.split("\n")
lines = len(doc_lines)
print('file is ' + str(lines) + ' lines long')
frequences = {}
max_length = max([len(w) for w in d])
for i in range(lines):
    for w in d:
        frequences[(w,i)] = conta(w,doc_lines[i])
print(frequences)

for j in range(max_length):
    print(' ',end='')

# for l in range(lines):
#     print('{}\t'.format(str(l)),end='')
# print()
# for w in d:
#     print(w,end='')
#     for j in range(max_length-len(w)):
#         print(' ',end='')
#     for l in range(lines):
#         print('{}\t'.format(str(frequences[(w,l)])),end='')
#     print()

g = 3
for l in range(round(lines/g)):
    print('{}\t'.format(str(l)),end='')
print()
for w in d:
    printed = ""
    print(w,end='')
    for j in range(max_length-len(w)):
        print(' ',end='')
    for l in range(round(lines/g)):
        somma = 0
        for _l in range(l,l+g):
            somma += frequences[(w,_l)]
        printed += str(somma) + '\t'
    print('{}\t'.format(printed,end=''))
