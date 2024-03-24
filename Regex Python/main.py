import re
str="akhil anil arun ankit"
res=re.findall(r'a[n][\w]*',str)
print(res)