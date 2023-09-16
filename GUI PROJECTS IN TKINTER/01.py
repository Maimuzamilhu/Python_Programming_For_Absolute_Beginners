import tkinter as tk

Mywindows = tk.Tk()

Mywindows.title("Finder and Size")
Mywindows.geometry("500x250") 
#Mywindows.attributes("-toolwindow" ,True)
#----------- RIGHT FRAME-----------------------

Rframe = tk.Frame(Mywindows , bg='blue' , width=150 , padx=9)
Rframe.pack(side="right" , fill="y")

#-------------TOP FRAME----------------------

Topframe = tk.Frame(Mywindows , bg='light blue' , width=150 , height = 50)
Topframe.pack(side="top" , fill = "x")

#-------------------------------------------

Topframe1 = tk.Frame(Mywindows , bg='light blue' , width=150 , height = 50)
Topframe1.pack(side="top" , fill = "x")

#----------Button----------------------------------------------
#------------------------------------------------------------

FindNextbt = tk.Button(Rframe , Text = "Find Next" , width=10)
FindNextbt.pack(side = "top" , pady=(10 ,5 )) #top bottom spacr

#-------------Replace--------------------------------------

FindNextbt1 = tk.Button(Rframe , Text = "Replace" , width=10)
FindNextbt1.pack(side = "top"  , pady=(0,5 ))

#-------------Replace ALL--------------------------------------

FindNextbt2 = tk.Button(Rframe , Text = "ReplceALL" , width=10)
FindNextbt2.pack(side = "top"  ,  pady=(0 ,5 ))

#------------- Cancell--------------------------------------

FindNextbt3 = tk.Button(Rframe , Text = "Cancell" , width=10)
FindNextbt3.pack(side = "top" ,  pady=(0 ,5))

#+++================================================
#==================Top Frames=======================

lblfind = tk.label(Topframe , text = "Find what" ,padx =20)
lblfind.pack()
#-----------------------------
entfind = tk.Entry(Topframe , width=35)
entfind.pack(side="left")

#==================bottom Frames=======================

lblfind2 = tk.label(Topframe1 , text = "Replace with" ,padx =20)
lblfind2.pack()
#-----------------------------
entfind2 = tk.Entry(Topframe1 , width=35)
entfind2.pack(side="left")

Mywindows.mainloop()