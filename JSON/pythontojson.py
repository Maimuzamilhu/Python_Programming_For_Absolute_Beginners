import json as myjson

Mydict = {

    "Name" : "muzzamil",
    "FatherName" : "Khalid",
    "Age"       : 21,
    "Parents" : {"Father" : "Khalid" , "Fatherr" : "Khalidd"}
}

result=myjson.dumps(Mydict)
print(result)

#-----------------------------------

file = open("JSON/TXT.JSON", "r")
myjson.dumps(Mydict,file)

