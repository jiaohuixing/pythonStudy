import requests

#r = requests.get('http://www.baidu.com')
url = 'http://www.baidu.com'
#header设置
hd = {'User-agent':'123'}
r = requests.get(url,headers=hd);

print(r.request.headers)

#代理池
#pxs = {'http':'http://user:pass@10.10.10.1:12345'}
#r=requests.get(url,proxies=pxs);

#HTTP请求的返回状态，比如，200表示成功，404表示失败
print (r.status_code)
#HTTP请求中的headers
print (r.headers)
#从header中猜测的响应的内容编码方式
print (r.encoding)
#从内容中分析的编码方式（慢）
print (r.apparent_encoding)
#响应内容的二进制形式
print (r.content)