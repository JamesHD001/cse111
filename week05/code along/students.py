import csv
import os; os.system('cls')

def read_dictionary(filename, key_column_index):
    student_dict = {}
    with open(filename, 'rt') as students_info:
        csvreader = csv.reader(students_info,delimiter=",")
        next(csvreader)
        for row in csvreader:
            key_value = row[key_column_index]
            student_dict[key_value] = row
    return student_dict

def main():
    KEY_INDEX = 0
    NAME_INDEX = 1
    students = read_dictionary('students.csv', KEY_INDEX)
    user_inumber = input("Enter the student's I-Number: ")
    user_inumber = user_inumber.replace("-","")
    if not user_inumber.isdigit():
        print("Invalid I-Number")   
        if user_inumber in students:
            student = students[user_inumber]
            name = student[NAME_INDEX]
            print(f" The Student's name is {name}")
        else:
                print("No such Student!")
    elif len(user_inumber) != 9:
        print("An I-Number must be 9 digits long")       
        
if __name__== "__main__":
    main()