class Beer(object):
    """
    Sing the verses of '99 Bottles of Beer on the Wall'
    """
    def verse(self, x):
        """
        Sing a specific verse of '99 Bottles of beer on the wall.

        :param x: The verse to sing
        """
        bottles = range(0, 100)

        label = lambda x: 'No more' if x == 0 else str(x)
        pluralize = lambda x: 'bottle' if x == 1 else 'bottles'
        num_of_beers = lambda x: '{} of beer'.format(x)
        on_the_wall = lambda x: '{} on the wall'.format(x)

        curr = bottles[x] 
        nxt = bottles[x-1]

        num_labeled = '{} {}'.format(label(curr), pluralize(curr))
        nxt_labeled = '{} {}'.format(label(nxt), pluralize(nxt))

        if not curr:
            next_action = 'Go to the store and buy some more'
        else:
            what = 'it' if curr == 1 else 'one'
            next_action = 'Take {} down and pass it around'.format(what)

        return "{}, {}.\n{}, {}.\n".format(
            on_the_wall(num_of_beers(num_labeled)),
            num_of_beers(num_labeled).lower(),
            next_action,
            on_the_wall(num_of_beers(nxt_labeled).lower())
        )

    def sing(self, x, y=0):
        """
        Sing the specified range of verses of '99 Bottles of Beer on the Wall.

        :param x: The verse to start with
        :param y: The verse to end with, defaults to the 0th verse
        """
        return '\n'.join([self.verse(i) for i in xrange(x, y-1, -1)]) + '\n'

