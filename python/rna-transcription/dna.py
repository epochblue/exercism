class DNA(object):
    """
    The four nucleotides found in DNA are adenine (A), cytosine (C),
    guanine (G) and thymidine (T).
    The four nucleotides found in RNA are adenine (A), cytosine (C),
    guanine (G) and uracil (U).

    Given a DNA strand, its transcribed RNA strand is formed by replacing each
    nucleotide with its complement:

        G -> C
        C -> G
        T -> A
        A -> U
    """
    def __init__(self, sequence):
        self.sequence = sequence

    def to_rna(self):
        """
        Convert this strand of DNA into RNA
        """
        DNA_TO_RNA = dict(G='C', C='G', T='A', A='U')
        return ''.join([DNA_TO_RNA.get(n, ' ') for n in self.sequence])

