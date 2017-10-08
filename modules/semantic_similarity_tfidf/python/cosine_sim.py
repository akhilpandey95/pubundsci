# This Source Code Form is subject to the terms of the MPL
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/AkhilHector/pubundsci/blob/master/LICENSE.

import sys

def cosine_sim(sentence_one, sentence_two):
    return True

if __name__ == "__main__":
    sentence_a = "The cosmic space is entirely divided across the solar system"
    sentence_b = "The galaxy of this university is completely spreada across the solar system"
    print cosine_sim(sentence_a, sentence_b)
    print cosine_sim(sentence_b, sentence_a)
else:
    print "ERROR: please input some arguments"
    sys.exit(0)
