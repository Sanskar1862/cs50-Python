name = input("Name of the owner ")
# it works same as that of switch
match name:
    case "Harry":
        print("Gryffindor")

    case "Hermoine":
        print("Gryffindor")

    case "RON":
        print("Texas")

    case "Gola":
        print("Hola")

    case _:
        print("Invalid Choice")


number = int(input("Input a number "))
match number:
    case 80:
        print("wow")

    case 70:
        print("wewew")

    case 60:
        print("hbfchbc")

    case _:
        print("Invalid Choice")

