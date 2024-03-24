from tkinter import *
from tkinter import font
tk=Tk()

tk.title("My Window")
tk.geometry("500x500")
tk.wm_iconbitmap('dribbble_logo_icon_257000.png')
c=Canvas(tk,bg="blue",height=500,width=300,cursor='pencil')
list_font=list(font.families())
print(list_font)
c.pack()
tk.mainloop()