# This Source Code Form is subject to the terms of the MPL
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/AkhilHector/pubundsci/blob/master/LICENSE.

import sys
import math
import numpy as np

def join_the_ngrams(*args):
    result = [[a[i] for a in args] for i in xrange(len(min(args, key = len)))]
    return result

def gen_ngrams(sentence, n):
    ngrams = join_the_ngrams(*[sentence.split()[i:] for i in xrange(n)])
    return ngrams

if __name__ == "__main__":
    sentence_a = "The cosmic space is entirely divided across the solar system"
    sentence_b = "The galaxy of this university is completely spreada across the solar system"
    print gen_ngrams(sentence_a, 2)
    print gen_ngrams(sentence_b, 3)
else:
    print "ERROR: please input some arguments"
    sys.exit(0)
