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
    
    # TODO: Read Remaining fields
    
    return {"name":name,
            "dob":dob,
            "aadhar":aadhar,
            "class":std,
            "admission_number":admission_number
            }

# function to register a student to organization
def register_student():
    student = get_student_details()
    admission_number = student['admission_number']
    students_data[admission_number] = student

    # saving the student data to a file
    stream = open("data/student_data.json","w+")
    json.dump(students_data,stream)
    stream.close()
    

def print_student_detais():
    admission_number = input("Enter Student Admission Number: ")
    student = students_data.get(admission_number)
    
    #Todo: handle errors invalid admission number

    print("\n-- STUDENT DETAILS --\n")
    print(f"Name: {student.get('name')}")
    print(f"Date of Birth: {student.get('dob')}")
    print(f"Aadhar: {student.get('aadhar')}")
    print(f"Class: {student.get('class')}")
    
    # TODO: update the code for remaining fields

# main starts here
if __name__ == "__main__":
    # load existing student data
    students_data = load_student_data_from_file()

    #TODO:  create a menu 