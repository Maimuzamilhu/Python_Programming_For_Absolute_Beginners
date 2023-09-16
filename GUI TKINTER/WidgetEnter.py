import tkinter as tk

Mywindows= tk.Tk()
#---------------------------------
def read_text():
    txt = MyEntry.get()
    print(txt) #reads the text with get keyword
#---------------------------------------

rb = tk.Label(Mywindows,text="txt ")
rb.pack()

#------------------------------------
MyEntry=tk.Entry(Mywindows,show="*", font="arial 24")
MyEntry.pack()

#------------------------------------------

Mybutton = tk.Button(Mywindows,text="Read Text" , command=read_text)
Mybutton.pack()

#print(MyEntry.keys())
Mywindows.mainloop()