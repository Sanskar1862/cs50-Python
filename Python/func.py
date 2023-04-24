def main():
    name = input("Enter your name ")
    number = int(input("Enter a number "))
    hello(name)
    hello(number)
    hello()  # default value is given in parameter which is wow
    print(f"Sum of two values are {calc(5,6)}")
    print(f"Square value {square()}")


def hello(myName="Wow"):
    print(f"hello, {myName}")


def calc(x, y):
    return x+y


def square(x=4):
    return pow(x, 4)


main()
