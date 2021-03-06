import urllib.request
from http import cookiejar

print("第一种方法")
url="http://www.baidu.com"
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print('第二种方法')
request = urllib.request.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

#加一个cookie
print("第三种方法")
cj = cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(cj)
print(len(response3.read()))