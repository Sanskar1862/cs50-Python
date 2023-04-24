class Student:

    school = "St. Thomas" #Static Variable

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    @classmethod   #keyword used to represent a class method
    def info(cls,name):
        cls.school = name

    def avg(self): #it is a instance method as it has self in its parameter list
        return ((self.m1+self.m2+self.m3)/3)

    @staticmethod
    def information():
        print("This is a student class")
    def get_m1(self): #Getters or Accessors
        return self.m1

    def set_m1(self,value):  #Setters or Mutators
        self.m1 = value

s1 = Student(34,56,78)
s2 = Student(45,78,58)

# Student.school = "JVM"
Student.info("JVM")
print(Student.school)
# print(s2.school)
print(s1.avg())
print(s2.avg())
print(Student.information())