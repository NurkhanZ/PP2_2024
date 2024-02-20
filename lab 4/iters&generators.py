# 1
n = int(input())
generator_exp = (i*i for i in range(n+1))

for i in generator_exp:
    print(i, end=" ")

# 2
n = int(input())
generator_evens = (i for i in range(n+1) if i%2 == 0)

output = ''
for i in generator_evens:
    output += str(i) + ','
print(output[:-1])

# 3
def functionGenerator():
    n = int(input())
    generator_exp = (i for i in range(n+1) if i%3 == 0 and i%4 == 0)

    for i in generator_exp:
        print(i, end=" ")

functionGenerator()

# 4
a = int(input())
b = int(input())

def squares(a, b):
    while a <= b:
        yield a*a
        a += 1
for i in squares(a, b):
    print(i, end=" ")

#5
n = int(input())
def generator(n):
    a = n
    while a != -1:
        yield a
        a -= 1
for i in generator(n):
    print(i, end=" ")
