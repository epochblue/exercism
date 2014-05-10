class Beer(object):
    """
    Sing the verses of '99 Bottles of Beer on the Wall'
    """
    def verse(self, current):
        """
        Sing a specific verse of '99 Bottles of Beer on the Wall'.

        :param x: The verse to sing
        """
        templates = {
            '_': '{0} bottles of beer on the wall, {0} bottles of beer.\n'
                 'Take one down and pass it around, {1} bottles of beer on the wall.\n',

            '2': '{0} bottles of beer on the wall, {0} bottles of beer.\n'
                 'Take one down and pass it around, {1} bottle of beer on the wall.\n',

            '1': '{0} bottle of beer on the wall, {0} bottle of beer.\n'
                 'Take it down and pass it around, no more bottles of beer on the wall.\n',
            
            '0': 'No more bottles of beer on the wall, no more bottles of beer.\n'
                 'Go to the store and buy some more, 99 bottles of beer on the wall.\n'
        }
        next_ = current - 1
        return templates['_' if current > 2 else str(current)].format(current, next_)
        
    def sing(self, x, y=0):
        """
        Sing a range of verses of '99 Bottles of Beer on the Wall'.

        :param x: The verse to start with
        :param y: The verse to end with, defaults to the 0th verse
        """
        return '\n'.join([self.verse(i) for i in xrange(x, y-1, -1)]) + '\n'

