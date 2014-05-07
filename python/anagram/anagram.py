class Anagram(object):
    """
    Given a word and a list of possible anagrams, selects the correct sublist.
    """
    def __init__(self, word):
        self._word = word

    def match(self, words):
        """
        Given a list of words, filter out anything that isn't an anagram

        :param words: a list of words to test
        """
        anagrams = []
        w = sorted(self._word.lower())
        for word in words:
            w2 = sorted(word.lower())
            if self._word != word and w == w2:
                anagrams.append(word)

        return anagrams
            
