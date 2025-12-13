"""
Author: Henry Daniel James

Description:
This program creates attendance for organizations, forums and leaders.
Add students
Mark attendance (Present / Absent)
Save attendance to a file
Load attendance from a file
Show attendance report
"""

import csv
import datetime

def add_student(student_list, name):
    """Adds students to the list if not already recorded.
    Returns the updated list."""
    
    if name not in student_list:
        student_list.append(name)
        return student_list
    
def mark_attendance(attendance_dict, name, status):
    """
    Marks a student as Present or Absent.
    Returns the updated attendance dictionary.
    """
    attendance_dict[name] = status
    return attendance_dict


def calculate_attendance_percentage(records):
    """
    Calculates attendance percentage from a list of statuses.
    """
    if not records:
        return 0

    present_count = records.count("Present")
    total = len(records)

    return (present_count / total) * 100