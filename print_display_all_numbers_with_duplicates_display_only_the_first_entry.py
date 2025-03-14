# Initialize an empty list to store the numbers entered by the user.
numbers = []
# Loop 10 times, prompt the user to input numbers.
for i in range(10):
  numbers.append(int(input(f"Enter number {i + 1}: ")))

# Keep track of seen numbers.
# Store unique first occurrences.
# Process each number.
# If not seen before, add to unique and mark as seen.
# Print result