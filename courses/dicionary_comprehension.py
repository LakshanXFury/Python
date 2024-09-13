import random

names = ['Arlyn', 'Zephyra', 'Kaelan', 'Elysia', 'Thorne', 'Liora']

students_scores = {student:random.randint(1,100) for student in names}

print(f"Randomly generated student scores {students_scores}")

passed_students = {student:score for (student, score) in students_scores.items() if score > 60}


print(f"Student scores which is higher than 60 {passed_students}")