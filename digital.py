from tkinter import *
from tkinter.ttk import *
from time import strftime

rt = Tk()
rt.title("Lazy clock")

def cl():
    sec = strftime('%H:%M:%S %p')
    l.config(text = sec)
    l.after(1000, cl)
l=Label(rt, font=('cardo',150), background="purple", foreground="violet")
l.pack(anchor='center')
cl()
mainloop()




