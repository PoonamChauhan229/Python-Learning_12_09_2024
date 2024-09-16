# Read user input for the monetary value in US dollars and conversion rate
usd_amount = float(input("Enter the amount in US dollars: "))
conversion_rate = float(input("Enter the conversion rate (CAD per USD): "))

# Calculate the equivalent amount in Canadian dollars
cad_amount = usd_amount * conversion_rate

# Print the final amount in Canadian dollars
print(cad_amount)
