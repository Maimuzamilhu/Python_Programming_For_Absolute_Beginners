import tkinter as tk

#mywindows = tk.Tk()

#mywindows.mainloop() #keeps the windows visible

#-----Disply the widget button label on the windows-----

#======================How to add wedget====================

Mywindows  = tk.Tk()

Mylabel = tk.Label(Mywindows , text= "Hello Muzzamil Khalid") #create a label
Mylabel.pack()

Mybottom = tk.Button(Mywindows , text = "HI muzzamil") #create a buttom 
Mybottom.pack()

Mylabel.mainloop()


