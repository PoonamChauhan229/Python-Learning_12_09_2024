# Specify unit prices for each fruit
apple_price = 2.94
peach_price = 3.50
watermelon_price = 7.99

# Read user input for the number of each fruit
num_apples = int(input("Enter number of apples: "))
num_peaches = int(input("Enter number of peaches: "))
num_watermelons = int(input("Enter number of watermelons: "))

# Calculate total price
total_price = (num_apples * apple_price) + (num_peaches * peach_price) + (num_watermelons * watermelon_price)

# Print the total price
print(total_price)
