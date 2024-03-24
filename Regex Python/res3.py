# import re
# # str="Rahul got 75 marks, Vijay got 55 marks, whereas Subbu got 98 marks"
# # marks=re.findall('\d{2}',str)
# # print(marks)
# str='This is normal\nstring'
# print(str)
# str=r'This is normal\n string'
# print(str)
# reg=r'm\w\w'
# prog=re.compile(reg)
# str='pmnt cat rat bat pat'
# result=prog.search(str)
# print(result.group())


import re
# prog=re.compile(r'm\w\w')
# str='rat cat hat mat'
# print(type(str))
# print(type(prog))
# print(type(re))
# result=prog.search(str)
# print(type(result))
# print(result.group())

# str='mn ran mop run'
# res=re.search(r'w\w\w',str)
# # if res:
# #     print(res.group())
# if res is not None:
#     print(res.group())
# else:
#     print("NONE Found")
# res=re.findall(r'r\w\w',str)
# if res is not None:
#     print(res)
# else:
#     print("Found none")
# str='man sun mop run'
# str2='tan sun mop run'
# res=re.match(r'm\w\w',str)
# res2=re.match(r'm\w\w',str2)
# print(res.group())
# if res2 is None:
#     print("None Found at beginnig")
# else:
#     print(res2.group())
# pile=re.split(r'\s',str)
# print("type returned by split is ",type(pile))
# print(pile)
#
# str="Ahemdabad is a city in Gujarat of India"
# res=re.sub(r'Ahemdabad',"Rajkot",str)
# print(type(res))
# print(res)
# str="an apple a day keeps the doctor away"
# # res=re.findall(r'a[\w]*',str)
# # findall gives a list of all patterns matching
# res=re.findall(r'\ba[\w]*\b',str)
# str="The meeting will be conducted on 1st and 21st of every month"
# res=re.findall(r'\d[\w]*',str)
# str="one two three four five six seven 8 9 10"
#
# res=re.findall(r'\b\w{5}\b',str)
# for word in res:
#     print(word)
# #  search give only first element found, we need to group to obtain the result
# res=re.search(r'\b\w{5}\b',str)
# print(res.group())
# str="one two three four five six seven 8 9 10"
# #  \d{4,} stands for 4 or more numbers found in the string
# res=re.findall(r'\b\w{4,}\b',str)
# for word in res:
#     print(word)
str="one two three four five six teven"
# \Z stands for checking at the end of string
res=re.findall(r't[\w]*\Z',str)
print(res)
str="Nageshwara Rao: 9706612345"
res=re.search(r'\d+',str)
print(res.group())

res=re.search(r'\D+',str)
print(res.group())
str="ankit akhil anil arun puna"
# [nk] stands for n or k or both
res=re.findall(r'a[nk][\w]*',str)
print(res)
res=re.findall(r'ank[\w]*',str)
print(res)
str="Vijay 20 1-5-2001, Rohit 21 22-10-1990, Sita 22 15-09-2000"
res=re.findall(r'\d{2}-\d{2}-\d{4}',str)
print(res)
res=re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(res)
str="Hello World"
res=re.search(r"^He",str)
if res:
    print("String starts with He")
else:
    print("String does not start with He")
str="Hello World"
# res=re.search(r'world$',str)
res=re.search(r'world|World$',str)
if res:
    print("String ends with 'world'")
else:
    print("String does not end with 'world'")
str="Hello World"
res=re.search(r'world$',str,re.IGNORECASE)
if res:
    print("String ends with 'World'")
    print(res.group())
else:
    print("String does not end with 'world'")
str='Rahul got 75 marks, Vijay got 55 marks, Om got 98 marks'
res=re.findall(r'\d{2}',str)
print(type(res))
res=re.findall('\d{2}',str)
print(type(res))
print(res)
# names=re.findall('[A-Z][a-z]*',str)
names=re.findall('[A-Z][a-z]',str)
names=re.findall('[A-Z]',str,re.IGNORECASE)
names=re.findall('[a-z]',str,re.IGNORECASE)
names=re.findall('[A-Z]*',str,re.IGNORECASE)
names=re.findall('[a-z]*',str,re.IGNORECASE)

names=re.findall('[A-Z]',str)
names=re.findall('[a-z]',str)
names=re.findall('[A-Z]*',str)
names=re.findall('[a-z]*',str)
print(names)

str="The meeting is at 2pm or 3am or 6pm or 7pm or 12am"
res=re.findall(r'\dam|\dpm',str)
print(len(res))