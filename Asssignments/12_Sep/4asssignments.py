# Read user input for the ploidy level and the number of chromosome sets
ploidy_level = int(input("Enter the ploidy level: "))
chromosome_sets = int(input("Enter the number of chromosome sets: "))

# Calculate the total number of chromosomes
total_chromosomes = ploidy_level * chromosome_sets

# Print the total number of chromosomes
print(total_chromosomes)
