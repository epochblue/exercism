import collections

def word_count(phrase):
    """Given a phrase, count the occurrences of each word in that phrase."""
    return collections.Counter(phrase.split())

