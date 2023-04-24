# print("hello")

# name = input("Enter name")
# print("Hello,",name)

# print(f"Hello,{name}")

n = int(input("Number"))
"""input by default always take a input"""
#so if we will not provide int it will give na error 
#as we are doing comparison between a string and a zero
if n>0:
    print("+ve")
elif n<0:
    print("n is -ve")    
else:
    print("0")

print("Hello,","Hello","Hello",(n+n),"\n")    
print("")

name = input("Enter name ")
print(f"Hello,{name}")
# Removes all whitespaces from start and end but not from mid
name = name.strip()
print(f"Hello,{name}")
# to capitalize 1st alphabet in string and all others in lowercase
name = name.capitalize()
print(f"Hello,{name}")
# helps to capitalize 1st alphabet of each letter in the word in the sentence
name = name.title()
print(f"Hello,{name}")

# Or
name = name.strip().title()
print(f"Halo, {name}\n\n\n")

splitName = "Hello what is your name"

splitName = splitName.split()
print(f"The Splitted line is {splitName}") 