class Student:
    name = ""
    house = ""
    # constructor
    def __init__(self, name, house = "Ranchi"):
        if not name:
            raise NameError("Missing Name")
        if house not in ["Gryffindor","Fufflepuff","Ranchi","Bokaro"]:
            raise ValueError("INVALID CHOICE")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house} using __str__ function"

    def charm(self):
        if self.name == "Sanskar":
            return "sanskar"

def main():
    student = get_Student()
    print(f"{student.name} from {student.house}")
    print(student)


def get_Student():
    # student = Student()
    # student.name = input("Enter the name")
    # student.house= input("Enter the house")
    name = input("Enter Name ")
    house = input("enter House ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main()
