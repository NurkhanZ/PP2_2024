# #1
gram = float(input())
def gram_to_ounce(gram):
    ounce = gram / 28.3495231
    return ounce
print(gram_to_ounce(gram))

# #2
F = int(input())
def fahrenheit_to_celsius(F):
    C = (5/9) * (F-32)
    return C
print(fahrenheit_to_celsius(F))

# #3
numheads = int(input())
numlegs = int(input())
def solve(numheads, numlegs):
    numrabbits = (numlegs - 2*numheads)/2
    numchickens = numheads - numrabbits
    return numchickens, numrabbits
print(solve(numheads,numlegs))

# #4
input_string = input("Enter a list of elements separated by space ")
mylist = input_string.split()
def isPrime(number):
    for i in range(2, int(int(number)/2)+1):
        if int(number)%i == 0:
            return False
    return True
def filter_prime(mylist):
    return [i for i in mylist if isPrime(i)]
print(*filter_prime(mylist))

#5
def permute(data, i, length):
    if i == length:
        print(''.join(data) )
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permute(data, i+1, length)
            data[i], data[j] = data[j], data[i]

string = str(input())
n = len(string)
data = list(string)
permute(data, 0, n)

# 6
string = str(input())
s = string.split()
s.reverse()
print(*s)

# 7
n = int(input())
array = []
for i in range(0, n):
    element = int(input())
    array.append(element)

def has_33(nums):
    for i in nums:
        if nums[i] == 3 and nums[i+1] == 3:
            print("True")
            return 0
    print("False")

has_33(array)

#8
n = int(input())
array = []
for i in range(0,n):
    ele = int(input())
    array.append(ele)

def spy_game(nums):
    count = 0
    has00 = False
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
        if count >= 2:
            has00 = True
        if has00 == True and nums[i] == 7:
            print("True")
            return 0
    print("False")
spy_game(array)

#9
import math
r = int(input())
V = 4/3 * math.pi * pow(r, 3)
print(V)

#10
n = int(input())
array = []
for i in range(0,n):
    ele = int(input())
    array.append(ele)

def unique_list(nums):
    unique = []
    for x in nums:
        if x not in unique:
            unique.append(x)
    print(*unique)
unique_list(array)

#11
s = str(input())
s1 = s[::-1]
if s == s1:
    print("is palindrom")
else:
    print("isn't palindrom")

#12
n = int(input())
array = [4,9,7]
for i in range(0,n):
    ele = int(input())
    array.append(ele)

def histogram(nums):
    for i in nums:
        print('*'*i)
histogram(array)

#13
import random
s = str(input("Hello! What is your name?" + "\n"))

x = random.randrange(1, 20, 1)
count = 1
print("\n" + "Well, " + s + ", I am thinking of a number between 1 and 20.")
while True: 
    print("Take a guess.")
    n = int(input())
    if n < x:
        print("\n" + "Your guess is too low")
        count += 1
    elif n > x:
        print("\n" + "Take upper is too high")
        count += 1
    else:
        print("\n" + "Good job, " + s + "! You guessed my number in " + str(count) + " guesses!")
        break 