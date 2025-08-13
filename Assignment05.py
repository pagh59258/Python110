# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   PAlves,8/12/2025,Created Script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #

#Import JSON Python module

import json

# Define the Data Constants

MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
students_on_file: list = [] #shows current student registrations saved on file
pend_save: str = ''

# When the program starts, read the JSON file data into a list of lists (table)
# Extract the data from the file

##file = open(FILE_NAME, "r")
##for row in file.readlines():
##    # Transform the data from the file
##    student_data = row.split(',')
##    student_data = [student_data[0], student_data[1], student_data[2].strip()]
##    # Load it into our collection (list of lists)
##    students.append(student_data)
##file.close()

# Loading JSON file content into students list

try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()

except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')

except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')

finally:
    if file.closed == False:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("Enter your menu choice number: ")

    # Input user data
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Input Error: Student's first name must be alphanumeric!")
            else:
                student_last_name = input("Enter the student's last name: ")
                if not student_last_name.isalpha():
                    raise ValueError("Input Error: Student's last name must be alphanumeric!")
                else:
                    course_name = input("Please enter the name of the course: ")
                    if course_name == "":
                        raise ValueError("Input Error: Course Name cannot be blank!")

        except ValueError as e:
            print("-" * 65)
            print(e)
            print("-" * 65)
            continue

        except Exception as e:
            print("-" * 65)
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
            print("-" * 65)

        student_data = {'FirstName':student_first_name,
                        'LastName':student_last_name,
                        'CourseName':course_name}
        students.append(student_data)
        print("-" * 65)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        print("-" * 65)
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"* 65)
        print("Here is the list of students currently registered for courses:")
        print("-"* 65)
        for student in students:
            print(f"{student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}.")
        print("-"* 65)
        print("IMPORTANT")
        print("- Some of these registrations might not be yet saved to file")
        print("- Make sure you use menu option 3 to save all registrations to file")
        print("-"* 65)
        continue

    # Save the data to a JSON file
    elif menu_choice == "3":

        try:
            #  Save the data to the file
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=2)
            file.close()

        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')

        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')

        finally:
            if file.closed == False:
                file.close()

        print("-"* 65)
        print("The following data was saved to file:")
        print("-"* 65)
        for student in students:
            print(f"{student['FirstName']} {student['LastName']} ,"
                  f"is enrolled in {student['CourseName']}.")
        print("-"* 65)
        continue

    # Stop the loop
    elif menu_choice == "4":
        #Check if there are information not yet saved on file
        file = open(FILE_NAME, "r")
        students_on_file = json.load(file)
        file.close()
        if(len(students) != len(students_on_file)):
            print("-" * 65)
            print("Warning: There are students registrations not yet saved on file.")
            print("-" * 65)
            pend_save=input("Do you want to save the data? (y/n): ")
            if(pend_save == "y"):
                file = open(FILE_NAME, "w")
                json.dump(students, file, indent=2)
                file.close()
                print("-" * 65)
                print("Thank you for saving the data!")
                print("-" * 65)
            else:
                print("-" * 65)
                print("As per your choice, pending registrations will not be saved to file!")
                print("-" * 65)
        break  # closes loop and terminate script execution
    else:
        print("-"* 65)
        print("Input Error: Please only choose option 1, 2, 3, or 4")
        print("-"* 65)

print("-"* 65)
print("Assignment05.py Python Script Execution Successfully Terminated")
print("-" * 65)