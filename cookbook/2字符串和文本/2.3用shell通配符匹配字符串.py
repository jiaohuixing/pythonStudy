#在python中使用linuxshell中的通配符如 *。py, Dat[0-9]*.py

from fnmatch import  fnmatch,fnmatchcase
print(fnmatch('foo.txt','*.txt'))
print(fnmatch('foo.txt','?oo.txt'))
print(fnmatch('Dat45.csv','Dat[0-9]*'))

names = ['Dat1.csv','Dat2.csv']
print([name for name in names if fnmatch(name,'Dat*')])