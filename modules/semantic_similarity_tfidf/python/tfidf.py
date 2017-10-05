# This Source Code Form is subject to the terms of the MPL
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/AkhilHector/pubundsci/blob/master/LICENSE.

import sys
import nltk
import string
from nltk import word_tokenize as tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer as stemmer

def stem_the_sentence(tokens):
    return [stemmer().stem(token) for token in tokens]

def tokenize_the_sentence(sentence):
    # create a dict and stem every token in a given sentence
    remove_punct_map = dict((ord(characters), None) for characters in string.punctuation)
    return stem_the_sentence(tokenize(sentence.lower().translate(remove_punct_map)))

def gen_similarity_score(sentence_one, sentence_two):
    sim_score = 0.0
    vectorizer = TfidfVectorizer(tokenizer = tokenize_the_sentence, stop_words = "english")

    # genreate the vectors and print the similarity score
    tfidf = vectorizer.fit_transform([sentence_one, sentence_two])
    sim_score = ((tfidf * tfidf.T).A)[0, 1]
    return sim_score

if __name__ == "__main__":
    sentence_a = "The cosmic space is entirely divided across the solar system"
    sentence_b = "The galaxy of this university is completely spreada across the solar system"
    print gen_similarity_score(sentence_a, sentence_b)
    print gen_similarity_score(sentence_b, sentence_a)
else:
    print "ERROR: please input some arguments"
    sys.exit(0)
