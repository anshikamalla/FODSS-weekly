"""
The below program takes a integer value from the user and says weather it is odd or even

"""
# Taking input from the user
num = int(input("Enter a number: "))

# Checking if the number is even or odd
if (num % 2 == 0):
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
