import tkinter as tk

Mywindows= tk.Tk()
#--------------------------
def FocusEntry():
    MyEntry.insert(0,"HI")

    MyEntry.focus()
#---------------------
Mybutton = tk.Button(Mywindows, text="Focus First" , command=FocusEntry)
Mybutton.pack()

#--------------------
MyEntry = tk.Entry(Mywindows)
MyEntry.pack()

#------------------
Myinsert = MyEntry.insert(0,"HI")




Mywindows.mainloop()