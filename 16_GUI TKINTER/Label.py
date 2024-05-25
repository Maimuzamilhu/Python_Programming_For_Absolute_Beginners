import tkinter as tk

Mywindows = tk.Tk()

#lbl  = tk.Label(Mywindows) 


Mywindows.configure(bg="light green"  ,bd =20 , relief="solid")
lbl  = tk.Label(Mywindows , text="Hi! Muzzamil\n How are you",bg="light blue" , bd =2, relief="solid" , font="Calibri 36" , height=6 , width=20 , justify="center" , padx=0 ,pady=0 , anchor="nw")


#lbl["text"] = "Hello! Muzzamil Khalid" #dict mehtod


#print("Label Options:" , lbl.keys()) #will shows all the labels


lbl.pack()

Mywindows.mainloop()