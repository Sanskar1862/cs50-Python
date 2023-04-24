i=3
for i in [1,2,3,4,5]:
    print("hello")

for i in range(3):
    print("hlo")

# we can even use loop without a variable
for _ in range(5):
    print("l")

# printing all elements of list using len

students = ["jnc","gc","gy"]

for i in range(len(students)):
    print(f"{students[i]}")

cars = {
    "BMW m3":470,
    "BMW m2":410,
    "BMW m5":600,
    "BMW m8":625
    }

print(cars["BMW m2"])

for car in cars:
    print(car)

for car in cars:
    print(car,cars[car])

students = {
    "Hermione":["Gryffindor","Otter"],
    "Harry":["Gryffindor","Stag"],
    "Ron":["Gryffindor","Jack Russes"],
    "Draco":["Slytherin",None]
}

for student in students.values():
    print(student[0],student[1],sep = " -> ")


