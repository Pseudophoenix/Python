import re
f=open('filename.txt','r')
# f.write("This project is assigned to Mr Alok at alok1234@gmail.com, and in case of any queries, you can contact Mr Mahesh Babu at \n Mahesh.k@gmail.com, or Ms Meena Kumar at veena@project.com who would be acting as assistant project coordinator.")
for line in f:
    res=re.findall(r'\S+@\S+',line)
    if len(res) > 0:
        print(res)
f.close()