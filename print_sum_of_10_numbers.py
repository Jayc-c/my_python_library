# Initialize the sum variable to 0, as a starting point.
sum = 0
# Loop 10 times, using 'i' in range to 10.
for i in range(10):
    # Ask the user to input a number per loop
    num = float(input(f"enter a number {i+1}"))
    # Add the input number to the sum variable.
    sum += num
# Print the sum of all the numbers.