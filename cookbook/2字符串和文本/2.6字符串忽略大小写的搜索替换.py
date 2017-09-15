import  re
text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python',text,flags=re.IGNORECASE))
print(re.sub('python','snake',text,flags=re.IGNORECASE))