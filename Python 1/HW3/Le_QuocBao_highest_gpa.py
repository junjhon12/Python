# Define a class for a GingerbreadHouse with an access method
class GingerbreadHouse:
    def access(self):
        print("Accessing the GingerbreadHouse")

# Define a Vector class for vector operations
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    # Define addition operation for vectors
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return Vector(new_x, new_y, new_z)

# Attempt to get user input for division, handle possible errors
try:
    user_num = int(input(':> '))  # User input for numerator
    div_num = int(input(':> '))  # User input for denominator
    result = user_num / div_num  # Perform division
except ValueError as e:
    print(f"Error: {e}. Enter Numeric GPA.")  # Handle non-integer input
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")  # Handle division by zero

# Open a file for appending and write new data
with open('student_grades.txt', 'a') as file:
    file.write("New data to append\n")

# Define an exception class for an empty roster
class EmptyRosterError(Exception):
    pass

# Define a Student class with methods to get GPA and name
class Student:
    def __init__(self, first_name, last_name, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa

    def get_first(self):
        return self.first_name

    def get_last(self):
        return self.last_name

# Define a Course class to manage student roster and operations
class Course:
    def __init__(self):
        self.roster = []  # Initialize an empty roster

    # Add a student to the roster
    def add_student(self, student):
        self.roster.append(student)

    # Get the number of students enrolled
    def course_size(self):
        return len(self.roster)

    # Find the student with the highest GPA in the roster
    def find_student_highest_gpa(self):
        if not self.roster:
            raise EmptyRosterError("Exception: Course Roster is Empty")
        return max(self.roster, key=lambda student: student.get_gpa())

# User interaction part to input student information
course = Course()  # Create a Course object
stop_word = ("quit", "q")  # Define stop word to exit input loop
while True:
    first_name = input("Enter your first name ('quit', or 'q' to exit): ")
    if first_name.lower() in stop_word:
        break
    last_name = input("Enter your last name: ")
    try:
        gpa = float(input("Enter GPA: "))
        student = Student(first_name, last_name, gpa)
        course.add_student(student)
    except ValueError:
        print("Invalid input for GPA. Skipping this student.")
    print()  # Add a line break for better readability

# Check if any students are enrolled and display the top student's information
if course.course_size() > 0:
    highest_gpa_student = course.find_student_highest_gpa()
    print(f"Course Size: {course.course_size()} students")
    print(f"Top Student: {highest_gpa_student.get_first()} {highest_gpa_student.get_last()} with GPA: {highest_gpa_student.get_gpa()}")
else:
    print("No students enrolled.")

# Access the GingerbreadHouse class and invoke the access method
gingerbread_house = GingerbreadHouse()
gingerbread_house.access()
