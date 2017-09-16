for i in range(1,3):
    print(i)

def frange(start,stop,increment):
    x=start
    while x<stop:
        yield x
        x+=increment
for i in frange(0,4,0.5):
    print(i)