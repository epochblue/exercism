import operator

class Series(object):
    """
    When given a string of digits, calculate the largest product for a series
    of consecutive digits of length n.
    """
    def __init__(self, series):
        self._series = map(int, list(series))

    def slices(self, size):
        if not size or size > len(self._series):
            raise ValueError('Invalid slice length for this series: %s' % size)

        series = self._series
        enum = enumerate(series)
        return [series[i:i+size] for i, _ in enum if i+size <= len(series)]

    def largest_product(self, length):
        if not length:
            return 1

        slices = self.slices(length)
        return max([reduce(operator.mul, slice, 1) for slice in slices])

