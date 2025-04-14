
"""

    This program accepts a list of names (entered as comma-separated values) and returns
    the sorted order of the names.
    
"""

def sorted_names(names_list):
    # Returns the list of names sorted in alphabetical order
    return sorted(names_list)

if __name__ == "__main__":
    names_input = input("Enter names separated by commas: ")
    # Create a list by stripping whitespace from each name
    names_list = [name.strip() for name in names_input.split(',')]
    sorted_list = sorted_names(names_list)
    print("Sorted names:", sorted_list)
