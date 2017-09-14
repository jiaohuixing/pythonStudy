text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah','yep'))

# 复杂的模式，使用re模块的sub功能
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import  re
print(re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2-',text))

#更复杂的功能，可以自定义函数
from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{}{}{}'.format(m.group(2),mon_name,m.group(3))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(change_date,text))