#1
class InputString(object):
    def __init__(self):
         self.s = ""

    def getString(self):
         self.s = input()

    def printString(self):
         print(self.s.upper())

strObj = InputString()
strObj.getString()
strObj.printString()

#2
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length * self.length

n = int(input())
aSquare = Square(n)
print(aSquare.area())

#3
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, l, w):
        Shape.__init__(self)
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width

l = int(input())
w = int(input())
aRectangle = Rectangle(l, w)
print(aRectangle.area())

#4
import math
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def showX(self):
        return self.x

    def showY(self):
        return self.y

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

#5
class Account:
    def __init__(self):
        print("Please write owner's name")
        self.balance = 0
        self.owner = input()
        print("Hello " + self.owner + ", please make an operation")

    def deposit(self):
        amount = float(input())
        self.balance += amount
        print("\nAmount deposited: ", amount)

    def withdraw(self):
        amount = float(input())
        if self.balance >= amount:
            self.balance -= amount
            print("\nAmount withdrawn: ", amount)
        else:
            print("\nInsufficient balance ")

    def display(self):
        print("\nNet balance available = ", self.balance)

aAccount = Account()

aAccount.deposit()
aAccount.withdraw()
aAccount.display()

#6
array = [0, 1, 2, 3, 4, 5, 6]

def prime(mylist):
    nums = mylist
    for i in range(2, 6):
        nums = filter(lambda x: x == i or x % i, nums)
    return nums

print(prime(array))
