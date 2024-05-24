# def max_score(studs):
#     top=""
#     max=0
#     for i in studs:
#         if studs[i]>max:
#             max=studs[i]
#             top=i
#     print(f"the class toper is {i} with {max} marks")

def grades(students):
    for i in students:
        if 91<=students[i]<=100:
            print (f"{i} : Outstanding")
        if 81<=students[i]<=90:
            print (f"{i} : Exceeds Expectations")
        if 71<=students[i]<=80:
            print (f"{i} : Acceptable")
        if 61<=students[i]<=70:
            print (f"{i} : Fail")
        

students_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88,
    "Eve": 95
}

grades(students_marks)