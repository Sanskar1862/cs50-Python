import statistics
import sys

print(statistics.mean([10,20,30,40]))
print(statistics.mode([10,20,30,40]))
print(statistics.median([10,20,30,40]))

try:
    print("hello , my name is ",sys.argv[1])
except IndexError:
    print("Too few arguments")

if len(sys.argv) < 2:
    print("Too few arugments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
else:
    print("Hello my name is ",sys.argv[1])

