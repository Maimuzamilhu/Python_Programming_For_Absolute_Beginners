import tkinter as tk

Mywindows =  tk.Tk()

Mylabel  = tk.Label(Mywindows,text="Hello Broh! Please Waster more Time")
Mylabel.pack()

Mylabel2  = tk.Label(Mywindows,text="Wil You? ")
Mylabel2.pack()

Mybutton  = tk.Button(Mywindows,text="Yes")
Mybutton.pack()

Mybutton1  = tk.Button(Mywindows,text="No")
Mybutton1.pack()

Mywindows.mainloop()