import random

names = ["Alex", "Beth", "Caroline", "Eleanor", "Dave", "Freddie"]

upper_case_list = [name.upper() for name in names if len(name) > 4]

students_score = {name:random.randint(0, 100) for name in names}

passed_students = {student:students_score[student] for student in students_score if students_score[student] > 60}

print(students_score)
print(passed_students)