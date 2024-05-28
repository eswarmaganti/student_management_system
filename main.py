import json
from pprint import pprint

# function to load student data from json file
def load_student_data_from_file():
    stream = open("data/student_data.json")
    return json.load(stream)


# get the student admission number
def get_admission_number():
    student_count = len(students_data.keys())+1
    curr_student_number = f'{student_count}'.zfill(4)
    admission_number = '2024'+curr_student_number

    return admission_number


# read the student data from keyboard
def get_student_details():
    print("\n -- ENTER STUDENT DETAILS -- \n")
    name = input("Enter student name: ")
    dob = input("Enter student Date of Birth: ")
    aadhar = input("Enter student aadhar: ")
    std = input("Enter student class: ")
    admission_number = get_admission_number()
    
    print("\nAddress Details")
    village = input("Enter village name: ")
    mandal = input("Enter mandal name: ")
    district = input("Enter district name: ")
    state = input("Enter state name: ")

    print("\nParent Details")
    father_name = input("Enter father's name: ")
    father_occupation = input("Enter father's occupation: ")

    # TODO: Read Remaining fields
    
    return {"name":name,
            "dob":dob,
            "aadhar":aadhar,
            "class":std,
            "admission_number":admission_number,
            "address": {
                "village": village,
                "mandal": mandal,
                "district": district,
                "state": state
            },
            "parent_details":{
                "father":{
                    "name": father_name,
                    "occupation": father_occupation,
                }
            }
            }

# function to register a student to organization
def register_student():
    
    student = get_student_details()

    # add new student to student_data
    admission_number = student['admission_number'] # student.get("admission_number")
    students_data[admission_number] = student

    # saving the student data to a file
    stream = open("data/student_data.json","w+")
    json.dump(students_data,stream)
    stream.close()
    

# function to print a student details
def print_student_detais():
    admission_number = input("Enter Student Admission Number: ")

    #check whether the admission number is valid or invalid
    if admission_number not in students_data.keys():
        print(f"*** Error: Invalid admission number : {admission_number} entered ***")
        return
    
    student = students_data.get(admission_number)
    print("\n-- STUDENT DETAILS --\n")
    print(f"Name: {student.get('name')}")
    print(f"Date of Birth: {student.get('dob')}")
    print(f"Aadhar: {student.get('aadhar')}")
    print(f"Class: {student.get('class')}")
    
    # TODO: update the code for remaining fields

# functions to print all student details
def print_all_students_details():
    for student in students_data.values():
        print(f"\n-- STUDENT DETAILS of {student.get('admission_number')} --\n")
        print(f"Name: {student.get('name')}")
        print(f"Date of Birth: {student.get('dob')}")
        print(f"Aadhar: {student.get('aadhar')}")
        print(f"Class: {student.get('class')}")

# main starts here
if __name__ == "__main__":
    # load existing student data
    students_data = load_student_data_from_file()

    #TODO:  create a menu 
    print(" STUDENT MANAGEMENT SYSTEM")
    print()
    print("1. Register New Student")
    print("2. Print Student Details")
    print("3. Print All Students Details")
    print("4. Update Student Details")
    print("5. Delete Student")

    choice =  int(input("Enter your choice: "))

    if choice == 1:
        register_student()
    elif choice ==2 :
        print_student_detais()
    elif choice == 3:
        print_all_students_details()
    elif choice == 4:
        pass
    else:
        print("*** Error: Invalid choice entered as input ***")