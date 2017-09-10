import xml.etree.ElementTree as ET

data = '''
<person>
<name>jack</name>
<password hide='true'></password>
<users>
<user>
<name>aaa</name><age>111</age>
</user>
<user>
<name>bbb</name><age>222</age>
</user>
</users>
</person>
'''

tree = ET.fromstring(data)
print('name',tree.find('name').text)
users = tree.findall('users/user')
for item in users:
    print(item.find('name').text,item.find('age').text)