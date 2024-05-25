import tkinter as tk
#==========Formula=================
def Calc():

    C= float(LblCelsius.get())

    f = (C*1.8) + 32
#LblCelsius3["text"] = str(f)+"*F"

#============================
MyWindows = tk.Tk()
#---------------------------
MyWindows.title("C TO F")
MyWindows.geometry("500x250")
#============Frames===============================

TopFrame = tk.Frame(MyWindows ,bg="blue" , width=100 , height= 40 , padx=5 , pady=5)
TopFrame.pack(side  = "top" , fill="x")

#----------------------------------------
TopFrame2 = tk.Frame(MyWindows ,bg="light blue" , width=100 , height= 40 , padx=5 , pady=5)
TopFrame2.pack(side  = "top" , fill="x")

#-------------------------------------------
TopFrame3 = tk.Frame(MyWindows ,bg="blue" , width=100 , height= 40 , pady=5)
TopFrame3.pack(side  = "top" , fill="x")

#==============wedght=================================
#-----------TOP-FRAMES LABEL----------------------------

LblCelsius = tk.Label(TopFrame , text="Celsius" , width=10 , anchor="w")
LblCelsius.pack(side="left")

#-----------Entry----------------------------

LblCelsius = tk.Entry(TopFrame , width=40)
LblCelsius.pack(side="left")


#---------------------------------------

LblCelsius2 = tk.Label(TopFrame2 , text="Ferhnite" , width=10, anchor="w")
LblCelsius2.pack(side="left")

#-----------Entry--------------------------

LblCelsius2 = tk.Label(TopFrame2 ,text ="--" ,font="arial 20")
LblCelsius2.pack(side="left")


#-----------------Button----------------------

LblCelsius3 = tk.Button(TopFrame3 , text="Covert" , width=10 , command=Calc)
LblCelsius3.pack()


#=====================================================


#=====================================================


MyWindows.mainloop()