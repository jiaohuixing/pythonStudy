from datetime import  datetime
text = '2012-09-20'
y=datetime.strptime(text,'%Y-%m-%d')
z = datetime.now()
diff = z-y
print(diff)