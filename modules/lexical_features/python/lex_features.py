# This Source Code Form is subject to the terms of the MPL
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/AkhilHector/pubundsci/blob/master/LICENSE.

import re
import sys
from collections import Counter
from itertools import groupby
from nltk.stem.porter import PorterStemmer

"""
m1 - The number of all word forms a text consists
m2 - The sum of the products of each observed frequency to the power of two
     and the number of word types observed with that frequency
"""

def tokenize(sentence):
    return re.split(r"[^0-9A-Za-z\-'_]+", sentence)

def compute_yules_k_for_text(sentence):
    tokens = tokenize(sentence)
    counter = Counter(token.upper() for token in tokens)

    #compute number of word forms in a given sentence/text
    m1 = sum(counter.values())
    m2 = sum([frequency ** 2 for frequency in counter.values()])

    #compute yules k measure and return the value
    yules_k = 10000/((m1 * m2) / (m2 - m1))
    return yules_k


def words_in_sentence(sentence):
    w = [words.strip("0123456789!:,.?()[]{}") for words in sentence.split()]
    return filter(lambda x: len(x) > 0, w)

def compute_yules_i_for_text(sentence):
    dictionary = {}
    stemmer = PorterStemmer()

    for word in words_in_sentence(sentence):
        word = stemmer.stem(word).lower()
        try:
            dictionary[word] += 1
        except:
            dictionary[word] = 1

    m1 = float(len(dictionary))
    m2 = sum([len(list(grouped_values)) * (frequency ** 2) for frequency, grouped_values in groupby(sorted(dictionary.values()))])

    # compute yules i and return the value
    yules_i = (m1 * m1) / (m2 - m1)
    return yules_i

if __name__ == "__main__":
    s = "The smoothing span is given by f. A larger value for f will result in a smoother curve. The number of robustifying iterations is given by iter. The function will run faster with a smaller number of iterations."
    print compute_yules_i_for_text(s)
else:
    sys.exit(0)
