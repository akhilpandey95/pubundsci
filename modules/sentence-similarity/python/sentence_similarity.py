# This Source Code Form is subject to the terms of the MPL
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/AkhilHector/pubundsci/blob/master/LICENSE.

import sys
import nltk
import string
from nltk.corpus import wordnet
from nltk import word_tokenize as tokenizer

def change_pos_tag(entity):
    try:
        if type(entity) == 'str' and entity[0] == 'J':
            changed_entity = 'a'
        elif type(entity) == 'str':
            changed_entity = string.lower(entity[0])
        else:
            changed_entity = None
    except:
        print "Unexpected error:"
        raise
    else:
        return changed_entity

def indentify_synset(word, pos_tag):
    try:
        word_net_tag = change_pos_tag(pos_tag)
        if word_net_tag is None:
            synset_item = None
        else:
            synset_item = wordnet.synset(word, word_net_tag)[0]
    except:
        print "Unexpect error:"
        raise
    else:
        return synset_item

def gen_similarity_score(sentence_a, sentence_b):
    try:
        # Init the variables
        similarity_score, simulation_count = 0.0, 0

        # POS tag and takenize the given sentences
        sentence_a = nltk.pos_tag(tokenizer(sentence_a))
        sentence_b = nltk.pos_tag(tokenizer(sentence_b))

        # Capture the synsets from the sentence and pass the unecessary args
        # into a new empty dict
        synset_of_senta = [identify_synset(*word) for word in sentence_a]
        synset_of_sentb = [identify_synset(*word) for word in sentence_b]

        for synset in synset_of_senta:
            efficiency = max([synset.path_similarity(s) for s in synset_of_sentb])

        if efficiency is not None:
            similarity_score += efficiency
            simulation_count += 1

        similarity_score /= simulation_count
    except:
        print "Unexpected error:"
        raise
    else:
        return similarity_score

if __name__ == "__main__":
    sentence_a = "Woman, without her man, is helpless."
    sentence_b = "Woman! Without her, man is helpless!"
    print gen_similarity_score(sentence_a, sentence_b)
else:
    sys.exit(0)
