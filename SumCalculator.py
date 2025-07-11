# Input from user
n = int(input("Enter a number: "))

# Initialize sum variable
total = 0

# Loop from 1 to n (inclusive)
for i in range(1, n + 1):
    total += i

# Display the result
print("Sum of numbers from 1 to", n, "is:", total)
