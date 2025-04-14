'''
Student Class Implementation

This program implements a Student class with attributes such as id, name, address,
admission year, level, and section. It instantiates objects to take input
for all attributes and displays the output.
'''

class Student:
    """
    A class to represent a student with various attributes.
    
    Attributes:
        student_id (str): Unique identifier for the student
        name (str): Full name of the student
        address (str): Address of the student
        admission_year (int): Year of admission
        level (str): Current level of study
        section (str): Section or class division
    """
    
    def __init__(self, student_id="", name="", address="", admission_year=0, level="", section=""):
        """
        Initialize a Student object with given attributes.
        
        Args:
            student_id (str): Unique identifier for the student
            name (str): Full name of the student
            address (str): Address of the student
            admission_year (int): Year of admission
            level (str): Current level of study
            section (str): Section or class division
        """
        self.student_id = student_id
        self.name = name
        self.address = address
        self.admission_year = admission_year
        self.level = level
        self.section = section
    
    def input_details(self):
        """
        Take input from user for all student attributes.
        """
        print("\nEnter Student Details:")
        print("-" * 25)
        self.student_id = input("Enter Student ID: ")
        self.name = input("Enter Full Name: ")
        self.address = input("Enter Address: ")
        
        # Input validation for admission year
        while True:
            try:
                self.admission_year = int(input("Enter Admission Year: "))
                # Basic validation for year
                if 1900 <= self.admission_year <= 2100:
                    break
                else:
                    print("Please enter a valid year between 1900 and 2100.")
            except ValueError:
                print("Please enter a valid year (numeric value).")
        
        self.level = input("Enter Level: ")
        self.section = input("Enter Section: ")
    
    def display_details(self):
        """
        Display all attributes of the student.
        """
        print("\nStudent Information:")
        print("-" * 25)
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Admission Year: {self.admission_year}")
        print(f"Level: {self.level}")
        print(f"Section: {self.section}")

def main():
    # Create a student object
    student = Student()
    
    # Input student details
    student.input_details()
    
    # Display student details
    student.display_details()
    


# Execute the main function when script is run
if __name__ == "__main__":
    main()