import UnitTest


def main():

    try:
        assert UnitTest.square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")

    try:
        assert UnitTest.square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")

    try:
        assert UnitTest.square(0) == 0
    except AssertionError:
        print("0 squared was not 0")

if __name__ == "__main__":
    main()
