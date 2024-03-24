from tkinter import *
import time
root=Tk()
root.title('Canvas')
c=Canvas(root,bg='blue',height=500,width=300)
root.wm_iconbitmap('python_sphere_icon_icon_257068.ico')
id=c.create_line(0,50,100,50,100,100,200,100,200,50,300,50,width=4,fill='white')
# for i in range(100,200,10):
id=c.create_oval(100,100,200,200,fill='yellow',width=4)
time.sleep(1)
c.pack()
root.mainloop()

