# Prompt user to give two numbers.
num1 = int(input("Input a number: "))
num2 = int(input("Input a number: "))

# Find range start and end.
start = min(num1, num2) + 1
end = max(num1, num2)

# Print numbers in range.