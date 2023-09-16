import tkinter as tk

MyWindows = tk.Tk()

Myframe = MyWindows.geometry("500x400")

Myframe = tk.Frame(MyWindows, bg="light blue" , height=30, width=150 , bd=2 , relief= "solid" )
Myframe.pack()

lbel = tk.Label(Myframe ,text="Hi!")
lbel.pack()

MyWindows.mainloop()