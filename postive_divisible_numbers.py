# Get input from the user
num = int(input("Enter a positive integer:"))

# Print positive numbers divisible by the input
print(f"Postive numbers divisible by the {num}:")
for i in range(1, num + 1):  # Assuming we want to check up to 100
    if num % i == 0:
        print(i)
