def max_score(studs):
    """Finds the student with the highest marks."""
    top = ""
    max_score = 0
    for student, score in studs.items():
        if score > max_score:
            max_score = score
            top = student
    print(f"The class topper is {top} with {max_score} marks")

def grades(students):
    """Assigns grades based on marks."""
    for student, mark in students.items():
        if 91 <= mark <= 100:
            print(f"{student} : Outstanding")
        elif 81 <= mark <= 90:
            print(f"{student} : Exceeds Expectations")
        elif 71 <= mark <= 80:
            print(f"{student} : Acceptable")
        elif 61 <= mark <= 70:
            print(f"{student} : Fail")
        else:
            print(f"{student} : Fail (below 61)")

students_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88,
    "Eve": 95
}

grades(students_marks)
max_score(students_marks)
