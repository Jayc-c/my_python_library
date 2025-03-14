# Initialize odd_count variable to 0.
odd_count = 0
# Loop 10 times, using "i" in range to 10.
for i in range(10):
# Prompt the user to input a number per loop.
    number = int(input(f"Enter number {i + 1}: "))
# Check if the input number is divisible by 2, if yes, add 1 to the variable.
    if number % 2 != 0:
        odd_count += 1
# Print the amount of even numbers.