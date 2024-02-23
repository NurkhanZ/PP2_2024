#1
from functools import reduce
from operator import mul
s = input()
numbers = list(map(int,s.split()))

result = reduce(mul, numbers)
print(result)

#2
s = str(input())
def up_low(s):
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print("No. of upper case characters: %s"%u)
    print("No. of lower case characters: %s"%l)
up_low(s)

#3
string = str(input())
def isPalidrome(s):
    rev = ''.join(reversed(s))

    if(s == rev):
        print("Is a  palindrom")
        return 0
    print("Isn't a palindrom")
isPalidrome(string)

#4
import threading
from time import sleep
import math
print("Sample Input:")
n = int(input())
def some_function():

    u = math.sqrt(n)
    print("Sample Output:")
    print("Square root of %s after %s miliseconds is %s" % (n,millisecond,u))

def non_blocking_function(function, msec):
    def function_to_sleep():
        sleep(msec / 1000)
        function()

    thread = threading.Thread(target=function_to_sleep)
    thread.start()
millisecond = int(input())
non_blocking_function(some_function, millisecond)

#5
s = input()
numbers = tuple(map(int,s.split()))

print(all(numbers))


