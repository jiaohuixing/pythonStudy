from collections import defaultdict,OrderedDict
import  json
d=defaultdict(list)
d['a'].append('1')
d['a'].append(2)
d['b'].append(2)

d=defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(3)
# print(d)

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
for key in d:
    print(key,d[key])
x=json.dumps(d)
# print(x)

prices = {
    'ACME':1,
    'b':2,
    'c':3,
    'd':4
}
del prices['d']
print(prices)
prices['e'] = 's'
print(prices)