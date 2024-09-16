# Read user input for the number of vehicles
num_bicycles = int(input("Enter number of bicycles: "))
num_tricycles = int(input("Enter number of tricycles: "))
num_cars = int(input("Enter number of cars: "))
num_trucks = int(input("Enter number of trucks: "))

# Calculate the number of wheels for each vehicle type
bicycle_wheels = num_bicycles * 2
tricycle_wheels = num_tricycles * 3
car_wheels = num_cars * 4
truck_wheels = num_trucks * 10

# Calculate the total number of wheels
total_wheels = bicycle_wheels + tricycle_wheels + car_wheels + truck_wheels

# Print the total number of wheels
print(total_wheels)
