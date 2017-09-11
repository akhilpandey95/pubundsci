# This Source Code Form is subject to the terms of the MPL
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/AkhilHector/pubundsci/blob/master/LICENSE.

import sys
import nltk
import string
from nltk.corpus import wordnet

def change_pos_tag(entity):
    if entity.startswith('N'):
        return 'n'

    if entity.startswith('V'):
        return 'v'

    if entity.startswith('J'):
        return 'a'

    if entity.startswith('R'):
        return 'r'

    return None

def indentify_synset(word, tag):
    word_net_tag = change_pos_tag(tag)
    if word_net_tag is None:
        return None

    try:
        return wordnet.synsets(word, word_net_tag)[0]
    except:
        return None

def gen_similarity_score(sentence_a, sentence_b):
    # Init the variables
    similarity_score, simulation_count = 0.0, 0

    # POS tag and takenize the given sentences
    sentence_a = nltk.pos_tag(nltk.word_tokenize(sentence_a))
    sentence_b = nltk.pos_tag(nltk.word_tokenize(sentence_b))

    # Capture the synsets from the sentence and pass the unecessary args
    # into a new empty dict
    synset_of_senta = [indentify_synset(word, tag) for word,tag in sentence_a]
    synset_of_sentb = [indentify_synset(word, tag) for word,tag in sentence_b]

    synset_of_senta = [s for s in synset_of_senta if s]
    synset_of_sentb = [s for s in synset_of_sentb if s]

    for synset in synset_of_senta:
        efficiency = max([synset.path_similarity(s) for s in synset_of_sentb])

        if efficiency is not None:
            similarity_score += efficiency
            simulation_count += 1

    similarity_score /= simulation_count
    return similarity_score


if __name__ == "__main__":
    sentence_a = "Aluminium is part of a compound that is known to cause breast cancer."
    sentence_b = "Aluminium is responsible for breast cancer."
    print gen_similarity_score(sentence_a, sentence_b)
    print gen_similarity_score(sentence_b, sentence_a)
else:
    sys.exit(0)
