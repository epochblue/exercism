def hey(what):
    """
    Bob is a lackadaisical teenager. In conversation, his responses are limited.
    Bob answers 'Sure.' if you ask him a question. He answers 'Whoa, chill out!'
    if you yell at him. He says 'Fine. Be that way!' if you address him without
    actually saying anything. He answers 'Whatever.' to anything else.
    """
    what = what.strip()

    if what.isupper():
        return 'Whoa, chill out!'

    if what.endswith('?'):
        return 'Sure.'

    if not what:
        return 'Fine. Be that way!'

    return 'Whatever.'

