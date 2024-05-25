Myfiles = open("Muzzamilkhalid.txt" ,"w")

#Content=Myfiles.write("Hello Muzzamil\t\nHow are you Broh\n")
Myfiles.seek(10)#yh 10 space chor dy ga is mai apni mrzi sy space krwa skty
Content = Myfiles.writelines(["Hello Muzzamil" ,"\nHow are You" ,"\nwHERE YO FROM"])
Myfiles.close()

Myfiles = open("Muzzamilkhalid.txt" ,"r")
Content=Myfiles.read()
print(Content)



Myfiles.close()