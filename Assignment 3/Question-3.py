'''
Word Find and Replace Program

This program finds and replaces a specific word in a text file with another word.
The program prompts for the filename, the word to find, and the replacement word.
'''

def find_and_replace(filename, word_to_find, replacement_word):
    """
    Find and replace a specific word in a file.
    
    Args:
        filename (str): The name of the file to modify
        word_to_find (str): The word to search for
        replacement_word (str): The word to replace with
        
    Returns:
        int: The number of replacements made
    """
    try:
        # Open and read the file content
        with open(filename, 'r') as file:
            content = file.read()
        
        # Count occurrences before replacement
        occurrences = content.count(word_to_find)
        
        if occurrences == 0:
            print(f"The word '{word_to_find}' was not found in the file.")
            return 0
        
        # Replace the word
        modified_content = content.replace(word_to_find, replacement_word)
        
        # Write the modified content back to the file
        with open(filename, 'w') as file:
            file.write(modified_content)
            
        print(f"Successfully replaced {occurrences} occurrence(s) of '{word_to_find}' with '{replacement_word}'")
        return occurrences
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return 0
    except PermissionError:
        print(f"Error: Permission denied. Check if you have proper access rights.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

def main():
    # Get input from user
    filename = input("Enter the filename: ")
    word_to_find = input("Enter the word to find: ")
    replacement_word = input("Enter the replacement word: ")
    
    # Perform find and replace operation
    find_and_replace(filename, word_to_find, replacement_word)

# Execute the main function when script is run
if __name__ == "__main__":
    main()