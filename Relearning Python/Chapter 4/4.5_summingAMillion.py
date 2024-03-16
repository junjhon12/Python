# Date: 1/9/2024
# Make a list of numbers from 1 to 1,000,000
# Use min() and max()
# Use sum() to see how quickly Python can add a million numbers.

# list of numbers
numbers = list(range(1, 1000001))

# min() and max()
print(min(numbers))
print(max(numbers))

# for loop
for number in numbers:
    print(sum(numbers))