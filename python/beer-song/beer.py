class Beer(object):

    def verse(self, x):
        bottles = range(0, 100)

        pluralize = lambda x: 'bottle' if x == 1 else 'bottles'
        label = lambda x: 'No more' if x == 0 else str(x)
        take_what_down = lambda x: 'it' if x == 1 else 'one'
        num_of_beers = lambda x: '{} of beer'.format(x)

        curr = bottles[x] 
        nxt = bottles[x-1]

        num_labeled = '{} {}'.format(label(curr), pluralize(curr))
        nxt_labeled = '{} {}'.format(label(nxt), pluralize(nxt))
        if not curr:
            next_action = 'Go to the store and buy some more'
        else:
            what = take_what_down(curr)
            next_action = 'Take {} down and pass it around'.format(what)

        return "{} on the wall, {}.\n{}, {} on the wall.\n".format(
            num_of_beers(num_labeled),
            num_of_beers(num_labeled).lower(),
            next_action,
            num_of_beers(nxt_labeled).lower()
        )

    def sing(self, x, y=0):
        return '\n'.join([self.verse(i) for i in xrange(x, y-1, -1)]) + '\n'

