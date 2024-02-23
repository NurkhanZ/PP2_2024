import re

# 1
s = str(input())
p = re.compile('a[b]*') 
m = p.search(s)
print(m)

# 2
s = str(input())
p = re.compile('ab{3}|ab{2}')
m = p.search(s)
print(m)

# 3
s = str(input())
p = re.compile('^[a-z]+_[a-z]+$')
m = p.search(s)
print(m)

# 4
s = str(input())
p = re.compile('[A-Z][a-z]+')
m = p.search(s)
print(m)

# 5
s = str(input())
p = re.compile('a.*?b$')
m = p.search(s)
print(m)

# 6
s = str(input())
p = re.sub("[ ,.]", ":", s)
print(p)

# 7
s = str(input())
words = s.split('_')
camel = words[0] + ''.join(word.capitalize() for word in words[1:])
print(camel)

# 8
s = str(input())
p = re.findall("[A-Z][^A-Z]*", s)
print(p)

# 9
s = str(input())
p = re.findall("[A-Z][^A-Z]*", s)
print(*p)

# 10
s = str(input())
p = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
m = re.sub('([a-z0-9])([A-Z])', r'\1_\2', p).lower()
print(m)
