import re
import string

class Phrase(object):
    def __init__(self, phrase):
        punc = re.escape(string.punctuation)
        self._words = re.sub('[{}]'.format(punc), '', phrase)
    
    def word_count(self):
        counts = dict()
        for word in [w.lower() for w in self._words.split()]:
            if not counts.get(norm):
                counts[norm] = 0

            counts[norm] += 1

        return counts

