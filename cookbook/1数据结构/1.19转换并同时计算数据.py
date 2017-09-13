import os
#判断文件或者文件夹是否存在
# os.path.exists()
files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
    print('there be python')
else:
    print('sorry,no python')

s = ('ACME',50,123.45)
print(','.join(str(x) for x in s))
portfolio = [
{'name':'GOOG', 'shares': 50},
{'name':'YHOO', 'shares': 75},
{'name':'AOL', 'shares': 20},
{'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)