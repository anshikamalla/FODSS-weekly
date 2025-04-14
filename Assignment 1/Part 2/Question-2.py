"""
2. Write a program that prompts the user for two integer values and displays 
the results of the first number divided by the second, with exactly two decimal places displayed. [5]

"""

# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


if (num2 == 0):
    print("Error! Division by zero is not allowed.")
else:
    result = num1 / num2
    print(f"Result: {result:.2f}")

