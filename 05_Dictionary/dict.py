Mydict = {"Name":"Muzzamil" ,"Age":"21" ,"Ms" :False}

print(Mydict)

#-----------------------oR---------------------

Mydict = {
    "Name":"Muzzamil",
    "Age":"21",
    "Ms" :False
    }

print(Mydict)

#-----------------Dictionary Length------------------------------
print("----------------------------------!")

r = len(Mydict)
print(r)

#----------Read item -------------------------------
print("-----------------------------------------!")
#first method
r = Mydict["Name"]
print(r)

#------Second method------------

b =Mydict.get("Name")
print(b)

#----------------Third method------------
c = Mydict.keys()
print(c)
#-----------Fourth method---------------------
c = Mydict.values()
print(c)

print("-----------------------------------------------")
#----------Chage the item------------------

Mydict["Name"]="Khalid"
print(Mydict)

#----------update----------------
print("---------------------------")

Mydict.update({"Name":"Myself"})
print(Mydict)

#------------Delete-----------
print("---------------------------------------")

Mydict.pop("Name")
print(Mydict)

Mydict.popitem()
print(Mydict)