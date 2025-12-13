"""
Test file for Attendance System
Author: Henry Daniel James
"""

from attendance import add_student, mark_attendance, calculate_attendance_percentage, save_attendance_to_file, load_attendance_from_file
import os


def test_add_student():
    students = []
    updated = add_student(students, "Henry")
    assert "Henry" in updated
    assert len(updated) == 1


def test_add_duplicate_student():
    students = ["Henry"]
    updated = add_student(students, "Henry")
    #No duplicates
    assert updated == ["Henry"]
    assert len(updated) == 1


def test_mark_attendance():
    attendance = {}
    updated = mark_attendance(attendance, "Henry", "Present")
    assert updated["Henry"] == "Present"
    assert len(updated) == 1


def test_calculate_attendance_percentage():
    records = ["Present", "Absent", "Present", "Present"]
    percentage = calculate_attendance_percentage(records)
    assert percentage == 75.0


def test_calculate_empty_records():
    percentage = calculate_attendance_percentage([])
    assert percentage == 0
    

def test_save_and_load_attendance(tmp_path):
    # Use a temporary file to avoid clutter
    test_file = tmp_path / "test_attendance.csv"
    
    data = {
        "2025-12-11": {
            "Henry": "Present",
            "Alice": "Absent"
        }
    }

    # Save the data
    save_attendance_to_file(test_file, data)

    # Load the data back
    loaded_data = load_attendance_from_file(test_file)

    # Check that the loaded data matches the saved data
    assert loaded_data == data
