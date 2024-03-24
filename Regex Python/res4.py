import re
f1=open("Table",'r')
f2=open('Salaries.txt','w')

for line in f1:
    # res1=re.findall(r'\d{4}',line)
    # print(res1)
    res1 = re.search(r'\d{4}', line)
    print(res1.group())
    res2 = re.search(r'\d{5}', line)
    # res2=re.findall(r'\d{5}',line)
    print(res2.group())
    f2.write(res1.group()+"\t")
    f2.write(res2.group()+"\n")

f1.close()
f2.close()