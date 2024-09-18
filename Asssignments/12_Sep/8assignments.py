import doctest

def gene_comparison(chromosome1: str, chromosome2: str, start_position: int, end_position: int) -> bool:
    """
    Returns whether the genes located on the two chromosomes are the same.
    
    Note: a gene is part of a chromosome with a start and end position.
    
    Parameters:
    chromosome1 (str): The first chromosome sequence.
    chromosome2 (str): The second chromosome sequence.
    start_position (int): The start position of the gene (1-based index, inclusive).
    end_position (int): The end position of the gene (1-based index, inclusive).
    
    Returns:
    bool: True if the gene sequences are the same, False otherwise.
    
    Examples:
    >>> gene_comparison("ATCGGCTTAACGAT", "TECGGAATACGATC", 3, 5)
    True
    
    >>> gene_comparison("ATCGGCT", "TCCGGAA", 2, 6)
    False
    """
    # Convert 1-based indices to 0-based indices for Python slicing
    start_index = start_position - 1
    end_index = end_position  # end_index is inclusive, so we use it as is

    # Extract the gene sequences
    gene1 = chromosome1[start_index:end_index]
    gene2 = chromosome2[start_index:end_index]

    # Compare the two gene sequences
    return gene1 == gene2

# Run doctest to validate the function
if __name__ == "__main__":
    doctest.testmod()

# use this testcase
print(gene_comparison("ATCGGCTTAACGAT", "TECGGAATACGATC", 3, 5)) # >>True
print(gene_comparison("ATCGGCT", "TCCGGAA", 2, 6)) #>>False