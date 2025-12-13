from attendance import add_student, mark_attendance, calculate_attendance_percentage


def test_add_student():
    students = []
    students = add_student(students, "Henry")
    assert "Henry" in students


def test_mark_attendance():
    attendance = {}
    attendance = mark_attendance(attendance, "Henry", "Present")
    assert attendance["Henry"] == "Present"


def test_calculate_attendance_percentage():
    records = ["Present", "Absent", "Present", "Present"]
    percentage = calculate_attendance_percentage(records)
    assert percentage == 75.0
