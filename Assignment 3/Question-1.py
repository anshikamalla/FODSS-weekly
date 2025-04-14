'''
File Statistics Counter

This program reads a text file and counts the number of lines, words, and characters.
The program prompts the user to input a file name and displays the statistics.
'''

def count_file_statistics(filename):
   
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the entire content
            content = file.read()
            
            # Count characters
            char_count = len(content)
            
            # Reset file pointer to beginning to count lines and words
            file.seek(0)
            
            # Count lines
            lines = file.readlines()
            line_count = len(lines)
            
            # Count words by splitting the content by whitespace
            word_count = len(content.split())
            
            return (line_count, word_count, char_count)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return (0, 0, 0)
    except Exception as e:
        print(f"An error occurred: {e}")
        return (0, 0, 0)

def main():
    # Get filename from user
    filename = input("Enter the filename to analyze: ")
    
    # Get statistics
    lines, words, chars = count_file_statistics()
    
    # Display results if file was successfully processed
    if lines > 0 or words > 0 or chars > 0:
        print("\nFile Statistics:")
        print("-" * 20)
        print(f"Number of lines: {lines}")
        print(f"Number of words: {words}")
        print(f"Number of characters: {chars}")

# Execute the main function when script is run
if __name__ == "__main__":
    main()