#append read

Myfiles = open("Muzzamilkhalid.txt" ,"a+")

r = Myfiles.write("Read append in Python!")

Myfiles.seek(0)

r = Myfiles.read()
print(r)

Myfiles.close()