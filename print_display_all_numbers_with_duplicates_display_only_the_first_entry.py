# Initialize an empty list to store the numbers entered by the user.
numbers = []
# Loop 10 times, prompt the user to input numbers.
for i in range(10):
  numbers.append(int(input(f"Enter number {i + 1}: ")))

# Keep track of seen numbers.
seen = []
# Store unique first occurrences.
unique_first = []

# Process each number.
for num in numbers:
  # If not seen before, add to unique and mark as seen.
  if num not in seen:
    unique_first.append(num)
    seen.append(num)

# Print result
print(unique_first)