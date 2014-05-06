import re
import string
import collections

class Phrase(object):
    """
    A program that given a phrase will count the occurrences of each word
    in that phrase (excluding punctuation, and ignoring case).
    """
    def __init__(self, phrase):
        punc = re.escape(string.punctuation)
        self._words = re.sub('[{}]'.format(punc), '', phrase).lower()
    
    def word_count(self):
        return collections.Counter(self._words.split())

