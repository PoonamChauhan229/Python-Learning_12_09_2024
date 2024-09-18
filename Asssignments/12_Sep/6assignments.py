# Translation function
def translation(codons: list[str]) -> str:
    codon_dict = {
    "UUU": 'F', "UUC": 'F', "UUA": 'L', "UUG": 'L',
    "CUU": 'L', "CUC": 'L', "CUA": 'L', "CUG": 'L',
    "AUU": 'I', "AUC": 'I', "AUA": 'I', "AUG": 'M',
    "GUU": 'V', "GUC": 'V', "GUA": 'V', "GUG": 'V',
    "UCU": 'S', "UCC": 'S', "UCA": 'S', "UCG": 'S',
    "CCU": 'P', "CCC": 'P', "CCA": 'P', "CCG": 'P',
    "ACU": 'T', "ACC": 'T', "ACA": 'T', "ACG": 'T',
    "GCU": 'A', "GCC": 'A', "GCA": 'A', "GCG": 'A',
    "UAU": 'Y', "UAC": 'Y', "UAA": '',  "UAG": '',
    "CAU": 'H', "CAC": 'H', "CAA": 'Q', "CAG": 'Q',
    "AAU": 'N', "AAC": 'N', "AAA": 'K', "AAG": 'K',
    "GAU": 'D', "GAC": 'D', "GAA": 'E', "GAG": 'E',
    "UGU": 'C', "UGC": 'C', "UGA": '',  "UGG": 'W',
    "CGU": 'R', "CGC": 'R', "CGA": 'R', "CGG": 'R',
    "AGU": 'S', "AGC": 'S', "AGA": 'R', "AGG": 'R',
    "GGU": 'G', "GGC": 'G', "GGA": 'G', "GGG": 'G'
}
    peptide = ""
    for codon in codons:
        if codon in codon_dict:
            peptide += codon_dict[codon]
    return peptide

# Test Cases
# Test Case 1
print(translation(["UGG", "CUA", "UCC", "AUG"]))  # Expected Output: "WLSM"

# Test Case 2
print(translation(["UUU", "AAC", "GUA", "UAG"]))  # Expected Output: "FNV"
