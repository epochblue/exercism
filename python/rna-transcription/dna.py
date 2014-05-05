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
    DNA_TO_RNA = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }

    def __init__(self, sequence):
        self.sequence = sequence

    def to_rna(self):
        """
        Convert this strand of DNA into RNA
        """
        rna = []
        for n in self.sequence:
            rna.append(self.DNA_TO_RNA.get(n, ' '))
        
        return ''.join(rna)

