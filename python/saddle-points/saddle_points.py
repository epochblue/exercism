"""
A function that detects saddle points in a matrix.

A "saddle point" is greater than or equal to every element in its row
and the less than or equal to every element in its column. A matrix may
have zero or more saddle points.
"""
def saddle_points(matrix):
    """
    Returns the set of saddle points in a given matrix.

    :param matrix: list of rows of a matrix
    """
    if not all([len(r) == len(matrix[0]) for r in matrix]):
        raise ValueError('irregular matrix')

    points = []
    for row_idx, row in enumerate(matrix):
        row_max = max(row)
        for col_idx, col in enumerate(row):
            col_min = min(zip(*matrix)[col_idx])
            if col == row_max and col == col_min:
                points.append((row_idx, col_idx))

    return set(points)

