class Matrix(object):
    """
    Given a string in the given format, maintain a representation of
    the matrix.

    For example, given a string with embedded newlines like:

        > 9 8 7
        > 5 3 2
        > 6 6 7

    maintain this matrix representation:

            0  1  2
          |---------
        0 | 9  8  7
        1 | 5  3  2
        2 | 6  6  7
    """
    def __init__(self, matrix):
        self._rows = []
        for row in matrix.splitlines():
            self._rows.append([int(x) for x in row.split()])

    @property
    def rows(self):
        """ Return the rows of the matrix."""
        return self._rows

    @property
    def columns(self):
        """ Return the list of columns of the matrix."""
        return [list(x) for x in zip(*self._rows)]

