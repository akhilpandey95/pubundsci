# This Source Code Form is subject to the terms of the MPL
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/AkhilHector/pubundsci/blob/master/LICENSE.

import sys
import nltk
from nltk import pos_tag as postag
from nltk import word_tokenize as tokenize
from nltk import RegexpParser as parser

def draw_parse_tree(sentence):
    # init a list and store the modified as a list item
    mod_sentence = []
    mod_sentence.append(sentence)

    # iterate over the list and create a parse tree of the sentence
    for words in mod_sentence:
        # tokenize the sentence and attach pos tags to each word
        tokens = tokenize(words)
        tagged_words = postag(tokens)

        # use regexpparser of nltk to parse the pos tagged words and store in a nltk tree list
        chunk = r"""Chunk: {<RB.?>*<VB.?>*<NNP>}"""
        form_parsed_chunk = parser(chunk)
        tree = form_parsed_chunk.parse(tagged_words)
        tree.draw()
        return tree

def syntax_similarity_score(sentence_one, sentence_two):
    return sentence_one, sentence_two

if __name__ == "__main__":
    sentence_a = "Woman, without her man, is helpless.";
    sentence_b = "Woman! Without her, man is helpless!"
    # print syntax_similarity_score(sentence_a, sentence_b)
    print draw_parse_tree(sentence_b)
else:
    sys.exit(0)
