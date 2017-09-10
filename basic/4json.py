import json

data = '''
[
{"name":"aaa","age":"111"},
{"name":"bbb","age":"222"}
]
'''

jso = json.loads(data)

for item in jso:
    print(item['name'],item['age'])