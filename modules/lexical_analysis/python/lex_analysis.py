# This Source Code Form is subject to the terms of the MPL
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/AkhilHector/pubundsci/blob/master/LICENSE.

import sys
import nltk
import string
import nltk.corpus as corpus
from nltk.stem.snowball import SnowballStemmer as stem

def tokenize_and_return(sentence):
    # first plan to remove the low content words like "is, the, if etc"
    low_content_words = corpus.stopwords.words('english')
    low_content_words.extend(string.punctuation)
    low_content_words.append('')

    # now return the tokens from the sentence
    return [words.lower().strip() for words in nltk.word_tokenize(sentence)
            if words.lower().strip() not in low_content_words]

def stem_and_return(sentence):
    # take the tokenized words and return the stemmed words
    return [stem('english').stem(words)
            for words in tokenize_and_return(sentence)]

def gen_text_score(word_one, word_two):
    print "Generating text features"
    return word_one, word_two

if __name__ == "__main__":
    # gen_text_score(sys.argv[1], sys.argv[2])
    sentence_a = "Woman, without her man, is helpless."
    sentence_b = "Woman! Without her, man is helpless!"
    print tokenize_and_return(sentence_a)
    print stem_and_return(sentence_a)
else:
    print "ERROR: please input arguments"
    sys.exit(0)
