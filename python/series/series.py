class Series(object):
    """
    Write a program that will take a string of digits and give you all the
    possible consecutive number series of length `n` in that string.
    """
    def __init__(self, series):
        self._series = map(int, list(series))

    def slices(self, size):
        if not size or size > len(self._series):
            raise ValueError('Invalid slice length for this series: %s' % size)

        series = self._series
        enum = enumerate(series)
        return [series[i:i+size] for i, _ in enum if i+size <= len(series)]

