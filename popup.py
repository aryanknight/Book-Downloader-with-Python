from tkinter import *
import os
def lead2():
    m=''
    ss=Tk()
    backdir=os.getcwd()+'\\Data\\name.txt'
    ss.iconbitmap(os.getcwd()+'\\Images\\round.ico')
    ss.wm_title('Book Name')
    g=StringVar()
    def values():
        m=en.get()
        with open(backdir,'w') as f:
            f.write(m)
        ss.destroy()
    j=''    
    label=Label(ss,text="Enter Book Name")
    label.grid(row=0,column=0)
    en=Entry(ss,width=30,textvariable=g)
    en.grid(row=1,column=0,padx=20, pady=10)
    b3=Button(ss,text='Done',command=values)
    b3.grid(row=1,column=1)
    ss.mainloop()

def lead3():
    m=''
    ss=Tk()
    backdir=os.getcwd()+'\\Data\\count.txt'
    ss.iconbitmap(os.getcwd()+'\\Images\\round.ico')
    ss.wm_title('Book Number')
    g=StringVar()
    def values():
        m=en.get()
        with open(backdir,'w') as f:
            f.write(m)
        ss.destroy()
    j=''    
    label=Label(ss,text="Enter the Serial.No of the Book ")
    label.grid(row=0,column=0)
    en=Entry(ss,width=30,textvariable=g)
    en.grid(row=1,column=0,padx=20, pady=10)
    b3=Button(ss,text='Done',command=values)
    b3.grid(row=1,column=1)
    ss.mainloop()
