class Bob(object):
    """
    Bob is a lackadaisical teenager. In conversation, his responses are very limited.

    Bob answers 'Sure.' if you ask him a question.
    He answers 'Woah, chill out!' if you yell at him.
    He says 'Fine. Be that way!' if you address him without actually saying anything.
    He answers 'Whatever.' to anything else.
    """
    def hey(self, msg):
        """
        Say something to Bob, he'll respond in turn.

        :param msg: The message for Bob to respond to.
        """
        msg = msg.strip()

        if not msg:
            return 'Fine. Be that way!'

        if msg.isupper():
            return 'Woah, chill out!'

        if msg.endswith('?'):
            return 'Sure.'

        return 'Whatever.'

