# --------------------------------------------------------------------------- #
# Title: Assignment06
# Desc: This assignment demonstrates using Classes and Functions
# Change Log: (Who, When, What)
#   PAlves,8/20/2025,Created Script
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# ------------------------- Imports ----------------------------------------- #
# --------------------------------------------------------------------------- #
import json
from io import TextIOWrapper


# --------------------------------------------------------------------------- #
# ------------------- Define the Data Constants ----------------------------- #
# --------------------------------------------------------------------------- #
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"


# --------------------------------------------------------------------------- #
# ---------------------- Define the Global Data Variables ------------------- #
# --------------------------------------------------------------------------- #
menu_choice: str  # Hold the choice made by the user.
students: list = []  # a table of student data


# --------------------------------------------------------------------------- #
# -------------------------- Data Layer ------------------------------------- #
# --------------------------------------------------------------------------- #

# --------------------- FileProcessor class  -------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    PAlves, 8/20/2025,Created Class

    """

    # ---------------------- read_data_from_file function ------------------- #
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function read data from the JSON file into student_data list

        ChangeLog: (Who, When, What)
        PAlves, 8/20/2025,Created function

        :return: None
        """

        try:
            file: TextIOWrapper = open(file_name, "r")
            student_data = json.load(file)
            file.close()

        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before\
             running this script!", e)

        except Exception as e:
            IO.output_error_messages("There was a non-specific \
            error!", e)

        finally:
            if not file.closed:
                file.close()

        return student_data


    # --------------------- write_data_to_file function --------------------- #
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data onto the JSON file

        ChangeLog: (Who, When, What)
        PAlves, 8/20/2025,Created function

        :return: None
        """

        try:
            file: TextIOWrapper = open(file_name, "w")
            json.dump(student_data, file, indent=2)
            file.close()
            print("-" * 65)
            print("The following data was saved to file:")
            print("-" * 65)
            for student in student_data:
                print(f"{student['FirstName']} {student['LastName']} ,"
                      f"is enrolled in {student['CourseName']}.")
            print("-" * 65)

        except TypeError as e:
            IO.output_error_messages("Please check that the data is \
            a valid JSON format", e)

        except Exception as e:
            IO.output_error_messages("There was a non-specific\
             error!", e)

        finally:
            if not file.closed:
                file.close()


# --------------------------------------------------------------------------- #
# --------------------- Presentation Layer ---------------------------------- #
# --------------------------------------------------------------------------- #

# -------------------------- IO class  -------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user
    input and output

    ChangeLog: (Who, When, What)
    PAlves, 8/20/2025,Created Class
    """

    # ------------------ output_error_messages function --------------------- #
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        PAlves, 8/20/2025,Created function

        :return: None
        """
        print("-" * 65)
        print(message, end="\n\n")
        print("-" * 65)
        if error is not None:
            print("-" * 65)
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')
            print("-" * 65)

    # ------------------------ output_menu function ------------------------- #
    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        PAlves, 8/20/2025,Created function

        :return: None
        """
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.

    # ------------------- input_menu_choice function ------------------------ #
    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        PAlves, 8/20/2025,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Error: Please, choose only 1, 2, 3, or 4")

        except Exception as e:
            IO.output_error_messages(e.__str__())

        return choice

    # ----------------- input_student_data function ------------------------- #
    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and Course Name

        ChangeLog: (Who, When, What)
        PAlves, 8/20/2025,Created function

        :return: None
        """

        try:
            # Input the data
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("First name cannot contain numbers or be blank.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("Last name cannot contain numbers or be blank.")

            course_name = input("What is the course name? ")
            if course_name =="":
                raise ValueError("Course name should not be blank.")

            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)

            print("-"* 65)
            print("List of students currently registered for courses:")
            print("-"* 65)
            for student in students:
                print(f"{student['FirstName']} {student['LastName']} "\
                      f"is enrolled in {student['CourseName']}.")
            print("-"* 65)
            print("IMPORTANT")
            print("-Some of these registrations might not be yet saved to file")
            print("-Make sure you use save registrations to file before exit")
            print("-"* 65)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct "\
                                     "type of data!", e)

        except Exception as e:
            IO.output_error_messages("There was a non-specific\
             error!", e)

        return student_data

    # ----------- output_current_student_data function --------------------- #
    @staticmethod
    def output_current_student_data(student_data: list):
        """ This function Displays the current student data

        ChangeLog: (Who, When, What)
        PAlves, 8/20/2025,Created function

        :return: None
        """

        try:
            print("-" * 65)
            print("List of students currently registered for courses:")
            print("-" * 65)
            for student in student_data:
                print(f"{student['FirstName']} {student['LastName']} "\
                      f"is enrolled in {student['CourseName']}.")
            print("-" * 65)
            print("IMPORTANT")
            print("- Some of these registrations might not be yet saved")
            print("- Make sure you use save registrations before exit")
            print("-" * 65)


        except ValueError as e:
            IO.output_error_messages(e)

        except Exception as e:
            IO.output_error_messages("There was a\
             non-specific error!", e)


    # ------------- output_check_unsaved_student_data function -------------- #
    @staticmethod
    def output_check_unsaved_student_data(student_data: list):
        """ This function Checks if there are any unsaved student data

        ChangeLog: (Who, When, What)
        PAlves, 8/20/2025,Created function

        :return: None
        """

        rec_on_file: list = []  # a table of student data already saved on JSON file

        try:
            rec_on_file = FileProcessor.read_data_from_file(file_name=FILE_NAME\
                                                          ,student_data=rec_on_file)

            if (len(student_data) != len(rec_on_file)):
                print("-" * 65)
                print("Warning: There are registrations not yet saved.")
                print("-" * 65)
                pend_save = input("Do you want to save the data? (y/n): ")
                if (pend_save == "y"):
                    # Invoke FileProcessor.write_data_to_file function to save data
                    FileProcessor.write_data_to_file(file_name=FILE_NAME, \
                                                     student_data=students)
                    print("-" * 65)
                    print("Unsaved data was written to JSON file!")
                    print("-" * 65)

                else:
                    print("-" * 65)
                    print("Pending data were not saved to file!")
                    print("-" * 65)

        except ValueError as e:
            IO.output_error_messages(e)

        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)


# --------------------------------------------------------------------------- #
# ------------------ Script Main body --------------------------------------- #
# --------------------------------------------------------------------------- #

# When the program starts:
#      Read from the Json file to extract data
#      Load extracted/read data into student_data list of lists (table)

students = FileProcessor.read_data_from_file(file_name=FILE_NAME, \
                                             student_data=students)

# ------------ Infinite loop until menu_option 4 is chosen ------------------ #
while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # ---------- menu_option 1 display current student data ---------------- #
    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)
        continue

    # ---------- menu_option 2 get new student data ----------------------- #
    elif menu_choice == "2":
        IO.output_current_student_data(student_data=students)
        continue

    # ---------- menu_option 3 save student data to JSON file ------------- #
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, \
                                         student_data=students)
        continue

    # - menu_option 4 check unsaved data and break loop to finish script -- #
    elif menu_choice == "4":
        IO.output_check_unsaved_student_data(student_data=students)
        break

# --------------------------------------------------------------------------- #
# -------------------- End of script  --------------------------------------- #
# --------------------------------------------------------------------------- #