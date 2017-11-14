# This Source Code Form is subject to the terms of the MPL
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/AkhilHector/pubundsci/blob/master/LICENSE.

import re
import sys
import nltk
from itertools import groupby
from collections import Counter
from nltk.collocations import *
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

def compute_collocation_score(sentence_one, sentence_two, option):
    if option == "bi":
        tokens_for_one = nltk.wordpunct_tokenize(sentence_one)
        tokens_for_two = nltk.wordpunct_tokenize(sentence_two)
        finder_one = BigramCollocationFinder.from_words(tokens_for_one)
        finder_two = BigramCollocationFinder.from_words(tokens_for_two)
        result_one = finder_one.score_ngrams(nltk.collocations.BigramAssocMeasures().raw_freq)
        result_one = [(tuple(map(str.lower, values)), scores) for values, scores in result_one]
        result_two = finder_two.score_ngrams(nltk.collocations.BigramAssocMeasures().raw_freq)
        result_two = [(tuple(map(str.lower, values)), scores) for values, scores in result_two]
        matches = [keys for keys in set(result_one).intersection(set(result_two))]
        return len(matches)
    elif option == "tri":
        tokens_for_one = nltk.wordpunct_tokenize(sentence_one)
        tokens_for_two = nltk.wordpunct_tokenize(sentence_two)
        finder_one = TrigramCollocationFinder.from_words(tokens_for_one)
        finder_two = TrigramCollocationFinder.from_words(tokens_for_two)
        result_one = finder_one.score_ngrams(nltk.collocations.TrigramAssocMeasures().raw_freq)
        result_one = [(tuple(map(str.lower, values)), scores) for values, scores in result_one]
        result_two = finder_two.score_ngrams(nltk.collocations.TrigramAssocMeasures().raw_freq)
        result_two = [(tuple(map(str.lower, values)), scores) for values, scores in result_two]
        matches = [keys for keys in set(result_one).intersection(set(result_two))]
        return len(matches)
    else:
        return 0

if __name__ == "__main__":
    s = "The smoothing span is given by f. A larger value for f will result in a smoother curve. The number of robustifying iterations is given by iter. The function will run faster with a smaller number of iterations."
    a = "Although population-level genomic sequence data have been gathered extensively for humans similar data from our closest living relatives are just beginning to emerge. Examination of genomic variation within great apes offers many opportunities to increase our understanding of the forces that have differentially shaped the evolutionary history of hominid taxa. Here we expand upon the work of the Great Ape Genome Project by analyzing medium to high coverage whole-genome sequences from 14 western lowland gorillas (Gorilla gorilla gorilla) 2 eastern lowland gorillas (G. beringei graueri) and a single Cross River individual (G. gorilla diehli). We infer that the ancestors of western and eastern lowland gorillas diverged from a common ancestor approximately 261 ka and that the ancestors of the Cross River population diverged from the western lowland gorilla lineage approximately 68 ka. Using a diffusion approximation approach to model the genome-wide site frequency spectrum we infer a history of western lowland gorillas that includes an ancestral population expansion of 1.4-fold around 970 ka and a recent 5.6-fold contraction in population size 23 ka. The latter may correspond to a major reduction in African equatorial forests around the Last Glacial Maximum. We also analyze patterns of variation among western lowland gorillas to identify several genomic regions with strong signatures of recent selective sweeps. We find that processes related to taste pancreatic and saliva secretion sodium ion transmembrane transport and cardiac muscle function are overrepresented in genomic regions predicted to have experienced recent positive selection."
    b = "Please note: this list is intended as a resource for those of you who are interested in responding to other CEHG members&rsquo; works for the blog. Let the blog editor (kkanagaw@stanford.edu) know if there are other publications that should be added to the"
    print compute_yules_i_for_text(s)
    print compute_collocation_score(a, b, "tri")
else:
    sys.exit(0)
