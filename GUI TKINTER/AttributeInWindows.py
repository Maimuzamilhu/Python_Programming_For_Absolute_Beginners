import tkinter as tk

Mywindows =  tk.Tk()

Mywindows.title("This is Muzzamil From Milkyway")
Mywindows.resizable(width=True , height=True)

#Mywindows.geometry("width*height+x+y")
Mywindows.geometry("500x400+300+150")

#---------------Attribute----------------------->

Mywindows.attributes("-alpha" , 1)

#-----------Window type to toolwindow

Mywindows.attributes("-toolwindow" , False) #minimize and maximize and close the window

#------Put window on the top of other 

Mywindows.attributes("-topmost",True)



Mywindows.mainloop()