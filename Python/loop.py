# alt + `` for activity bar
def main():
    i = 50
    loop(i)
    triangle()

def loop(number):
    i = number
    while i != 0:
        if i%2 == 0:
            print(f"Hello,{i}")
        i -= 1

def triangle():
    r=0
    while r<5:
        c=0
        while c<r:
            print("* ",end="")
            c += 1

        print("")
        r+=1
main()