from datetime import  timedelta,datetime

a=timedelta(days=2,hours=6)
b=timedelta(hours=4.5)
c=a+b
print(c.days)
print(c.seconds)

print(c.total_seconds())

a=datetime(2012,9,23)
print(a+timedelta(days=10))

print(datetime.today())