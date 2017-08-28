#导入bs4模块
from bs4 import BeautifulSoup

html = '''
html
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href=http://example.com/elsie" class="sister" id="link1"/>Elsie,
<a href=http://example.com/lacie" class="sister" id="link2"/>Lacie and
<a href=http://example.com/tillie" class="sister" id="link3"/>Tillie;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</html>
'''

soup = BeautifulSoup(html,'html.parser')

print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])
print(soup.a)
print(soup.find(id='link1'))
for link in soup.find_all('a'):
    print(link.get('href'))
print(soup.get_text())

#soup = BeautifulSoup(html,'lxml')