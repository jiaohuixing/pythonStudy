s = ' hello world \n'
print(s.strip())
print(s.replace(' ',''))

import  re
print(re.sub('\s+',' ',s))