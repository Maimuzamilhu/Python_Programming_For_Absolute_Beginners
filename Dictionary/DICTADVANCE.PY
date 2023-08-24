Mydict = {"Name":"Muzzamil" ,"Age":"21" ,"Ms" :False}

print(Mydict)

#-----------------------oR---------------------

Mydict = {
    "Name":"Muzzamil",
    "Age":"21",
    "Ms" :False
    }
for k , v in Mydict.items():
    print(k,v)

#---------Copy-------------------------
print("------------------------------")

newdict = Mydict.copy()
print(newdict)