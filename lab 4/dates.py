import datetime
from datetime import date
from datetime import timedelta

#1
x = datetime.datetime.now()
print(x.day-5)

# 2
today = date.today()

yesterday = today - timedelta(days = 1)

tomorrow = today + timedelta(days = 1)

print(yesterday)
print(today)
print(tomorrow)

# 3
x = datetime.datetime.now()
print(x.microsecond)

#4
current_date = datetime.datetime.now()
y = int(input())
m = int(input())
d = int(input())
setdate = datetime.datetime(y,m,d,0,0,0)
newdate = current_date-setdate
print(newdate.total_seconds())


