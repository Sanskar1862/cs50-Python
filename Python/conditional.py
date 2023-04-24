def main():
    print(compare())
    compare1()   #no returning value
    print(boolComp())
    print(is_even(45))

def compare():
    x = 5
    y = 5
    if x > y:
        return "x is greater"
    elif y > x:
        return "y is greater"
    else:
        return "x == y"

def boolComp():
    x = 4
    y = 4
    if x == y :
        return True
    else:
        return False 

def compare1():
    n = int(input("Enter the number"))

    if n <= 90 and n > 80:
        print("A")

    elif n <= 80 and n > 70:
        print("B")

    elif n <= 70 and n > 60:
        print("C")

    else:
        print("F")


def is_even(n):
    return n%2 == 0


main()
