import json

people = [
    {"name" : "Harry", "house" : "Gryffindor"},
    {"name" : "Cho", "house":"ravenclaw"},
    {"name":"Draco", "house":"Slytherin"}
]

# def f(person):
#     return person["name"]

# people.sort(key = f)

# print(f"{people}",sep = "\n")


people.sort(key = lambda person:person["name"])

pretty = json.dumps(people, indent=4, sort_keys=True)
print(pretty)

