import tkinter as tk

Mywindows= tk.Tk()
#--------------------------
def FocusEntry():
    MyEntry.focus()
#---------------------
Mybutton = tk.Button(Mywindows, text="Focus First" , command=FocusEntry)
Mybutton.pack()

#--------------------
MyEntry = tk.Entry(Mywindows)
MyEntry.pack()
#------------------
MyEntry2 = tk.Entry(Mywindows)
MyEntry2.pack()
#-----------------
MyEntry3 = tk.Entry(Mywindows)
MyEntry3.pack()
#-----------------




Mywindows.mainloop()