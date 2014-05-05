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
        _rows = matrix.splitlines()
        self.rows = [[int(column) for column in row.split()] for row in _rows]

        _columns = zip(*self.rows)
        self.columns = [list(column) for column in _columns]

