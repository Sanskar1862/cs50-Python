# print(format("Welcome", "10s"),end= "#")
# print(format(111,"4d"),end="#")
# # print(format(924.656,"3.2f"))
# def of(x):
#     yield x+1
#     print("Tst")
#     yield x+2
# g = of(10)
# print(next(g))
# print(next(g))

# a = 10
# of()
# print("a =",a)

# e = "butter"
# def f(a):
#     print(a)+e
# f("bitter")
# class t():
# pass
# x = t()
# bool(x)
# sentence = "we are humanss"
# matched = re.match(r'(.*)(.*?)(.*)',sentence)
# print(matched.groups())


import time

t = (2009,2,17,17,3,38,1,48,0)
t = time.mktime(t)

print(time.strftime("%b %d %Y %H:%M:%S",time.gmtime(t)))


# import datetime

# mydate = datetime.date(2018,3,1)
# print(mydate.strftime("%A"))

# l = ["hello"]
# print(l)




# fo = open("foo.txt","wb")
# print ("Name of the file: ",fo.name)
# fo.flush()
# fo.close()




a = [2, 4, 6]

def solve():
   global a 
   a = [1, 3, 5]

print(a)
solve()
print(a)

numbers = (4, 7, 19, 2, 89, 45, 72, 22)
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# class fruits:
#     def __init__(self,price):
#         self.price = price

# obj=fruits(50)
# obj.quantity = 10
# obj.bags = 2

# print(obj.quantity+len(obj.__dict__))
# class A:
#     def __init__(self):
#         self.calcI(30)
#         print("i from A is",self.i)

#     def calcI(self,i):
#         self.i = 2*i;

# class B(A):
#     def __init_(self):
#         super().__init__()

#     def calcI(self,i):
#         self.i = 3*i;

# b = B() 