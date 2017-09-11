# This Source Code Form is subject to the terms of the MPL
# License. If a copy of the same was not distributed with this
# file, You can obtain one at
# https://github.com/AkhilHector/pubundsci/blob/master/LICENSE.

import sys
import nltk
import string
import nltk.corpus as corpus
from nltk.corpus import wordnet
from nltk.stem.snowball import SnowballStemmer as stem
from nltk.stem.wordnet import WordNetLemmatizer as wnl

low_content_words = corpus.stopwords.words('english')
low_content_words.extend(string.punctuation)
low_content_words.append('')

def tokenize_and_return(sentence):
    # now return the tokens from the sentence
    return [words.lower().strip() for words in nltk.word_tokenize(sentence)
            if words.lower().strip() not in low_content_words]

def stem_and_return(sentence):
    # take the tokenized words and return the stemmed words
    return [stem('english').stem(words)
            for words in tokenize_and_return(sentence)]

def check_for_tags_and_stopwords(word, tag):
    # check if a tag is Noun and if the word is not present in the low profile words
    if tag == wordnet.NOUN and word.lower().strip() not in low_content_words:
        return True
    else:
        return False

def tags_for_sent(sentence):
    return map(change_to_wordnet_tag, nltk.pos_tag(nltk.word_tokenize(sentence)))

def change_to_wordnet_tag(tag):
    if tag[1] == 'J':
        return (tag[0], wordnet.ADJ)
    elif tag[1] == 'V':
        return (tag[0], wordnet.VERB)
    elif tag[1] == 'N':
        return (tag[0], wordnet.NOUN)
    elif tag[1] == 'R':
        return (tag[0], wordnet.ADV)
    else:
        return (tag[0], wordnet.NOUN)

def gen_text_score(word_one, word_two):
    print "Generating similarity score"
    jacard_coefficient = 0.0

    lemma_for_senta = [wnl().lemmatize(word.lower().strip(), tag) for word, tag in tags_for_sent(sentence_a) if check_for_tags_and_stopwords(word, tag)]
    lemma_for_sentb = [wnl().lemmatize(word.lower().strip(), tag) for word, tag in tags_for_sent(sentence_b) if check_for_tags_and_stopwords(word, tag)]

    jacard_coefficient = len(set(lemma_for_senta).intersection(lemma_for_sentb)) / float(len(set(lemma_for_senta).union(lemma_for_sentb)))

    return jacard_coefficient

if __name__ == "__main__":
    # gen_text_score(sys.argv[1], sys.argv[2])
    # sentence_a = "my name is abhishek, i am a brother of akhil and i am also helpless."
    # sentence_b = "My name is akhil, i am helpless!"

    # sentence_a = "Drinking coffee can probably help improve the quality of life."
    # sentence_b = "According to a research study, drinking coffee will affect your health"

    sentence_a = "Drinking coffee can definitely help improve the quality of life."
    sentence_b = "According to a research study, drinking coffee can surely help in improving the quality of your life"

    # print tokenize_and_return(sentence_a)
    # print tokenize_and_return(sentence_b)
    # print stem_and_return(sentence_a)
    # print stem_and_return(sentence_b)
    print gen_text_score(sentence_a, sentence_b)
else:
    print "ERROR: please input arguments"
    sys.exit(0)
