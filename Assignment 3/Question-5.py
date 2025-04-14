'''
Word Occurrence Counter

This program counts the occurrence of each word in a text file.
The program ignores case sensitivity and punctuation for accurate word counting.
'''

import re
import string

def count_word_occurrences(filename):
    """
    Count the occurrence of each word in a file.
    
    Args:
        filename (str): The name of the file to analyze
        
    Returns:
        dict: A dictionary with words as keys and their counts as values
    """
    try:
        # Initialize an empty dictionary to store word counts
        word_counts = {}
        
        # Open and read the file
        with open(filename, 'r') as file:
            # Read file content
            content = file.read().lower()
            
            # Remove punctuation
            for punct in string.punctuation:
                content = content.replace(punct, ' ')
            
            # Split into words and count occurrences
            words = content.split()
            for word in words:
                # Strip any remaining non-alphanumeric characters
                word = re.sub(r'[^a-zA-Z0-9]', '', word)
                
                # Skip empty strings
                if not word:
                    continue
                    
                # Update word count
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
        
        return word_counts
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

def display_word_counts(word_counts):
    """
    Display word counts in a nicely formatted manner.
    
    Args:
        word_counts (dict): Dictionary containing words and their counts
    """
    if not word_counts:
        print("No words to display.")
        return
    
    # Sort words by occurrence (highest first)
    sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Find the longest word for formatting
    max_word_len = max(len(word) for word in word_counts.keys())
    
    # Display header
    print("\nWord Occurrences:")
    print("-" * (max_word_len + 15))
    print(f"{'Word'.ljust(max_word_len)} | Occurrences")
    print("-" * (max_word_len + 15))
    
    # Display each word and its count
    for word, count in sorted_counts:
        print(f"{word.ljust(max_word_len)} | {count}")
    
    print("-" * (max_word_len + 15))
    print(f"Total unique words: {len(word_counts)}")

def main():
    # Get filename from user
    filename = input("Enter the filename to analyze: ")
    
    # Count word occurrences
    word_counts = count_word_occurrences(filename)
    
    # Display results
    display_word_counts(word_counts)

# Execute the main function when script is run
if __name__ == "__main__":
    main()