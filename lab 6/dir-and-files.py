import os
import string
#1
path = r'C:\Users\User\Desktop\PP2'
print("Only directories:")
print([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])
print("\nOnly files:")
print([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))])
print("\nAll directories and files:")
print([name for name in os.listdir(path)])

#2
path_string = str(input())
path = path_string
print("Exist:", os.access(path, os.F_OK))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))

#3
path_string = str(input())
path = path_string
print("Test a path if it's exists:")
print(os.path.exists(path))
print("\nFile name of path")
print(os.path.basename(path))
print("\nDir name of path")
print(os.path.dirname(path))

#4
path_string = str(input())
path = path_string
def count_lines(fname):
    with open(fname) as f:
        for i,l in enumerate(f):
            pass
    return i + 1
print("Number of lines in file: ", count_lines(path))

#5
string = str(input())
s = string.split()

path = r'C:\Users\User\Desktop\PP2\lab 6\test.txt'

with open('test.txt', 'w+') as f:
    for items in s:
        f.write('%s\n' %items)
    print("File written successfully")
f.close()

#6
alphabet = string.ascii_uppercase
for letter in alphabet:
    with open(letter+'.txt', 'w') as f:
        f.write(letter)

#7
with open('test.txt','r') as firstfile, open('second_test.txt','a') as secondfile:
    for line in firstfile:
        secondfile.write(line)

#8
path_string = str(input())
path = path_string
print("Exist:", os.access(path, os.F_OK))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))
os.remove(path)
print("File has been deleted")


