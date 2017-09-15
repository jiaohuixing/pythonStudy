import  re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a 
multiline comment */
'''
print(comment.findall(text1))
print(comment.findall(text2))

#(?:.|\n) 指定了一个非捕获组
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

#re.DOTAIL
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))