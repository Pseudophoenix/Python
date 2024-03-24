import re
import urllib.request
f=urllib.request.urlopen(r'file:///C:\Users\alok4\Desktop\Regex\Reg1\breakfast.html')
test=f.read()
str=test.decode()
result=re.findall(r'<td>\w+</td>\s<td>(\w+)</td>\s<td>(\d\d)</td>',str)
print(result)
for item,price in result:
    print('Item=%-15s Price=%-10s' %(item,price))
f.close()
