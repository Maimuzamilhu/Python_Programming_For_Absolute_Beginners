import tkinter as tk

Mywindows = tk.Tk()

Mywindows.geometry("300x300")

TopFrame =  tk.Frame(Mywindows,bg="light blue" , width=100 , height=30)
TopFrame.pack(side ="top")
Mywindows.mainloop()