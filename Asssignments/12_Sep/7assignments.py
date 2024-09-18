def dna_transcription(dna: str) -> str:
    """
    Transcribes a DNA sequence into its corresponding RNA sequence.
    - A (Adenine) is replaced with U (Uracil)
    - T (Thymine) is replaced with A (Adenine)
    - C (Cytosine) is replaced with G (Guanine)
    - G (Guanine) is replaced with C (Cytosine)
    
    Parameters:
    dna (str): The DNA sequence to be transcribed (all caps).

    Returns:
    str: The transcribed RNA sequence (all caps).
    
    Examples:
    >>> dna_transcription("ATCG")
    'UAGC'
    >>> dna_transcription("GATTACA")
    'CUAAUGU'
    >>> dna_transcription("ATCTAC")
    'UAGAUG'
    """
    rna = ""
    
    for base in dna:
        if base == "A":
            rna += "U"
        elif base == "T":
            rna += "A"
        elif base == "C":
            rna += "G"
        elif base == "G":
            rna += "C"
        else:
            raise ValueError(f"Unexpected base: {base}")
    
    return rna

# If running this script directly, perform doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    # Directly calling the function and printing the result
    print(dna_transcription("ATCTAC"))  # This will print the result of the function call
    print(dna_transcription("GCGTAC")) 