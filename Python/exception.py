try:
    x = int(input("Enter a  number "))

except ValueError:
    print("X is not an integer ")

else:
    print(f"value -> {x}")

# in this we will keep on iterating untill i get an integer
while True:
    try:
        x = int(input("Enter a  number "))

    except ValueError:
        print("X is not an integer ")

    else:
        break

print(f"value -> {x}")

# or

while True:
    try:
        x = int(input("Enter a  number "))
        break

    except ValueError:
        # print("X is not an integer ")
        pass

print(f"value -> {x}")

n = 20
while n > 0:
    if n % 2 == 0:
        print(n)
    else:
        pass
    n -= 1
