"""

    This program accepts a string input from the user and calculates the number of uppercase
    and lowercase letters in the string.
    
"""

def count_upper_lower(s):
    # Initialize counters for uppercase and lowercase letters
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

if __name__ == "__main__":
    # Get input from the user
    user_input = input("Enter a string: ")
    upper, lower = count_upper_lower(user_input)
    print("Number of uppercase letters:", upper)
    print("Number of lowercase letters:", lower)
