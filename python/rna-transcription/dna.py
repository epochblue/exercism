from string import maketrans, translate

DNA = 'ACGT'
RNA = 'UGCA'
TRANSLATION = maketrans(DNA, RNA)

def to_rna(strand):
    """Translate the given DNA strand into an RNA strand."""
    return translate(strand, TRANSLATION)

