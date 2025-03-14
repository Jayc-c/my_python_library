# Create a loop iterating numbers from 0 to 100
for i in range(101):
# Check if the number ends in 0, by dividing to 10 and won't equal to 0.
    if i % 10 != 0 or i == 0:
# Print if the remainder is not equal to 0. It means the number doesn't end in 0.
        print(i)