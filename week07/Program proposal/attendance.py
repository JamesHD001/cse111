"""
Author: Henry Daniel James

Description:
Free Attendance Registration System.
This program helps organizations and groups track attendance by:
- Adding students
- Marking daily attendance (Present/Absent)
- Saving attendance to a CSV file
- Loading attendance from a CSV file
- Viewing attendance reports and percentages
"""

import csv
import datetime

#Program Logic
def add_student(student_list, name):
    """Adds a student if not already in the list."""
    if name not in student_list:
        student_list.append(name)
    return student_list


def mark_attendance(attendance_dict, name, status):
    """Marks a student as Present or Absent for the day."""
    attendance_dict[name] = status
    return attendance_dict


def calculate_attendance_percentage(records):
    """Calculates percentage from a list of attendance statuses."""
    if not records:
        return 0
    present_count = records.count("Present")
    return (present_count / len(records)) * 100


def save_attendance_to_file(filename, attendance_records):
    """
    Saves attendance to a CSV file in the format:
    date,student,status
    """
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Student", "Status"])

        for date, record in attendance_records.items():
            for student, status in record.items():
                writer.writerow([date, student, status])


def load_attendance_from_file(filename):
    """
    Loads attendance data from CSV into this structure:
    {
        "2025-01-01": {"Henry": "Present", "John": "Absent"},
        ...
    }
    """
    attendance_records = {}

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for date, student, status in reader:
                if date not in attendance_records:
                    attendance_records[date] = {}
                attendance_records[date][student] = status

    except FileNotFoundError:
        pass

    return attendance_records

def show_report(attendance_records):
    """Displays attendance summary and percentages."""
    if not attendance_records:
        print("No attendance records found.")
        return

    print("\n===== ATTENDANCE REPORT =====")

    all_students = set()
    all_statuses = {}

    for date, daily_records in attendance_records.items():
        for student, status in daily_records.items():
            all_students.add(student)
            all_statuses.setdefault(student, []).append(status)

    for student in sorted(all_students):
        records = all_statuses.get(student, [])
        percent = calculate_attendance_percentage(records)
        print(f"{student}: {percent:.2f}% Present  ({records})")

    print("=============================")

def save_attendance_to_file(filename, attendance_records):
    """Saves attendance records to a CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Student", "Status"])

        for date, records in attendance_records.items():
            for student, status in records.items():
                writer.writerow([date, student, status])

    print(f"Attendance saved to {filename} successfully.")


def load_attendance_from_file(filename):
    """Loads attendance from a CSV file back into the dictionary."""
    attendance_records = {}

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for date, student, status in reader:
                if date not in attendance_records:
                    attendance_records[date] = {}
                attendance_records[date][student] = status

        print(f"Attendance loaded from {filename} successfully.")
    except FileNotFoundError:
        print("No saved attendance file found.")

    return attendance_records


def show_attendance_report(attendance_records):
    """Displays all attendance in a readable format."""
    if not attendance_records:
        print("No attendance records found.")
        return

    print("\n===== ATTENDANCE REPORT =====")
    for date, records in attendance_records.items():
        print(f"\nDate: {date}")
        for student, status in records.items():
            print(f"  {student}: {status}")

def main():
    students = []
    attendance_records = {}

    while True:
        print("\n===== ATTENDANCE SYSTEM =====")
        print("1. Add Student")
        print("2. Mark Attendance for Today")
        print("3. Show Attendance Report")
        print("4. Save Attendance to File")
        print("5. Load Attendance from File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            add_student(students, name)
            print(f"{name} added successfully!")

        elif choice == "2":
            if not students:
                print("No students added yet!")
                continue

            today = datetime.date.today().isoformat()
            if today not in attendance_records:
                attendance_records[today] = {}

            print("Mark attendance for today:")
            for student in students:
                status = input(f"{student} (Present/Absent): ").capitalize()
                if status not in ["Present", "Absent"]:
                    print("Invalid input. Marked as Absent.")
                    status = "Absent"
                mark_attendance(attendance_records[today], student, status)

            print("Attendance recorded.")

        elif choice == "3":
            show_attendance_report(attendance_records)

        elif choice == "4":
            save_attendance_to_file("attendance.csv", attendance_records)

        elif choice == "5":
            attendance_records = load_attendance_from_file("attendance.csv")


        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
