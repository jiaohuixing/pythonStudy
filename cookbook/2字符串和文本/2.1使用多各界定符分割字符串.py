line = 'asdf fjdk; afed, fjek,asdf, foo'
import  re
print(re.split(r'[;,\s]\s*',line))
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
values = fields[::2]
print(values)
delemiters=fields[1::2]+['']
print(delemiters)


# 检查某个文件夹中是否存在指定的文件类型
# if any( name.endswith(('.c','.h')) for name in os.listdir(dir))