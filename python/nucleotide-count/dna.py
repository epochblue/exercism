class DNA(object):
    """
    Represents a strand of DNA, with methods for enumerating the nucleotides
    in each strand.
    """
    NUCLEOTIDES = ('A', 'G', 'C', 'T', 'U')

    def __init__(self, strand):
        self._strand = strand
        self._count = dict(A=0, G=0, C=0, T=0)

        for n in strand:
            self._count[n] = strand.count(n)

    def count(self, nucleotide):
        """
        Return the count of a specific nucleotide within the strand.
        """
        if nucleotide not in self.NUCLEOTIDES:
            raise ValueError('{} is not a nucleotide.'.format(nucleotide))

        return self._count.get(nucleotide, 0)

    def nucleotide_counts(self):
        """
        Return the counts of all nucleotides within the strand.
        """
        return self._count

