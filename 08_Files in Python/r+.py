Myfiles  = open("khalid.txt","r+")

r = Myfiles.write("Hello Muzzamil Khalid!")
r = Myfiles.seek(0)
r =Myfiles.read()
print(r)

Myfiles.close()