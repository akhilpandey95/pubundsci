# This Source Code Form is subject to the terms of the MPL
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/AkhilHector/pubundsci/blob/master/LICENSE.

import sys
import numpy as np
from math import sqrt, log
from collections import defaultdict
from itertools import chain, product

def vectorize(sentence, vocabulary):
    result = [sentence.split().count(i) for i in vocabulary]
    return result

def convert_words_to_vectors(sentence):
    vectorized_sentence = []
    vocabulary = sorted(set(chain(*[words.lower().split() for words in sentence])))
    for words in sentence:
        vectorized_sentence.append((words, vectorize(words, vocabulary)))
    return vectorized_sentence, vocabulary

def dot_product_of_vectors(vector_one, vector_two):
    result = np.dot(vector_one, vector_two) / (sqrt(np.dot(vector_one, vector_one)) * sqrt(np.dot(vector_two, vector_two)))
    return result

def cosine_sim(sentence_one, sentence_two):
    sentences = [sentence_one, sentence_two]
    corpus, vocabulary = convert_words_to_vectors(sentences)
    similarity = [dot_product_of_vectors(a[1], b[1]) for a, b in product(corpus, corpus)]
    return similarity[1]

if __name__ == "__main__":
    sentence_a = "The cosmic space is entirely divided across the solar system"
    sentence_b = "The galaxy of this university is completely spreada across the solar system"
    sentence_c = "Woman, without her man, is helpless.";
    sentence_d = "Woman! Without her, man is helpless!"

    print cosine_sim(sentence_a, sentence_b)
    print cosine_sim(sentence_c, sentence_d)
else:
    print "ERROR: please input some arguments"
    sys.exit(0)
