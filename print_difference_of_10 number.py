# Initialize an empty list
numbers = []
    # Loop 10 times, using 'i' in range to 10.
for i in range(10):
    # Ask the user to input a number per loop
    num = int(input(f"Enter number {i+1}: "))
    # Add the input number to the list.
    numbers.append(num)
# process
result = numbers[0] - sum(numbers[1:])
# Print the result of the first number minus all the remaining numbers.
print(f"The result is: {result}")