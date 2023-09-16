import tkinter as tk
#-------Function Area-------->
def Dl_file():
    print("The Download is Started!")
#----------------------------------
def Close_app():
    Mywindows.quit()

#==============================
Mywindows = tk.Tk()

labl = tk.Label(Mywindows, text="Click Here to Download")
labl.pack()
#===================================================================

lbl = tk.Button(Mywindows , text="Download" , command=Dl_file) #function name)

lbl.pack()

#=====================================================================
labelclose = tk.Button(Mywindows,text="Exit" , command=Close_app )
labelclose.pack()

#print("Button options :",lbl.keys())

Mywindows.mainloop()