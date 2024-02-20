import math
#1
degree = int(input("Input degree: "))
radians = degree * 0.0174533
print("Output radians: " + str(radians))

#2
height = int(input("Height: "))
base_a = int(input("Base, first value: "))
base_b = int(input("Base, second value: "))
area = (base_a + base_b)/2 * height
print("Expected Output: "+ str(area))

#3
num_sides = int(input("Input number of sides: "))
lenght_side = int(input("Input the length of a side: "))
area = num_sides * pow(lenght_side,2) * (1/4)
print("The area of the polygon is: " + str(area))

#4
base_lenght = int(input("Length of base: "))
height = int(input("Heigth of parallelogram: "))
area = base_lenght * height
print("Expected output: " + str(float(area)))
