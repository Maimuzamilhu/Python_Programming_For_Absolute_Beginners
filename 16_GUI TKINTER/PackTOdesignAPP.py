import tkinter as tk

Mywindows = tk.Tk()

Mywindows.geometry("300x300")
#------------------------------
Tbutt = tk.Button(Mywindows, text="Top Button" , bg = "light blue")
Tbutt.pack(side="bottom" , fill="x")   #top,left,right,bottom

Tbutt2 = tk.Button(Mywindows, text="left" , bg = "light blue")
Tbutt2.pack(side="left" , fill="y")

Tbutt = tk.Button(Mywindows, text="Top" , bg = "light blue")
Tbutt.pack(side="top" , fill="x")

Tbutt = tk.Button(Mywindows, text="right" , bg = "light blue")
Tbutt.pack(side="right" , fill="y")
#---------------------One more box_-----------

Tbutt = tk.Button(Mywindows, text="Top Button" , bg = "light yellow")
Tbutt.pack(side="bottom" , fill="x")

Tbutt2 = tk.Button(Mywindows, text="left" , bg = "light yellow")
Tbutt2.pack(side="left" , fill="y")

Tbutt = tk.Button(Mywindows, text="Top" , bg = "light yellow")
Tbutt.pack(side="top" , fill="x")

Tbutt = tk.Button(Mywindows, text="right" , bg = "light yellow")
Tbutt.pack(side="right" , fill="y")
#--------------------CENTER-----------------------------------


#Cenbutt = tk.Button(Mywindows, text="Center" , bg = "light gray")
#Cenbutt.pack(side="right")

#Cenbutt = tk.Button(Mywindows, text="Center" , bg = "light gray")
#Cenbutt.pack(side="right")

#Cenbutt = tk.Button(Mywindows, text="Center" , bg = "light gray")
#Cenbutt.pack(side="right")

#Cenbutt = tk.Button(Mywindows, text="Center" , bg = "light gray")
#Cenbutt.pack(side="right")

#---------------------top--------------------------------------

#Topbutt = tk.Button(Mywindows, text="Top" , bg = "light green")
#Topbutt.pack(side="top")

#Topbutt = tk.Button(Mywindows, text="Top" , bg = "light green")
#Topbutt.pack(side="top")

#Topbutt = tk.Button(Mywindows, text="Top" , bg = "light green")
#Topbutt.pack(side="top")

#
#Topbutt = tk.Button(Mywindows, text="Top" , bg = "light green")
#Topbutt.pack(side="top")

#=================================================
#==================Expand===========================

Topbutt = tk.Button(Mywindows, text="Top" , bg = "light blue")
Topbutt.pack(side="top",fill="both", expand=True)



Mywindows.mainloop()