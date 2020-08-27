rna_mapping = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}

def to_rna(dna_strand: str) -> str:
    return ''.join([rna_mapping[dna_unit] for dna_unit in dna_strand])
