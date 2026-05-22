'''students = ["Ron","Hermione","Harry"]
for student in students:
    print(student)'''


'''students = ["Ron","Hermione","Harry"]
for i in range(len(students)):
    print(i+1, students[i])'''



'''students = {
    "Hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")'''
    
    

students = [
    {"name":"Hermione", "house":"Gryffindor", "patronus":"otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"stag"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"jack russel terrier"},
    {"name":"Draco", "house":"Slytherin", "patronus":"None"} 
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
