from collections import  namedtuple
Subscriber=namedtuple('Subscriber',['addr','date'])
sub = Subscriber('jonesy@example.com','dd')
print(sub)