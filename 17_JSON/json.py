from aifc import Error
import json as MyJSON
import os

JsonString = '{"Name" : "Muzzamil" , "LastName" : "Khalid" : "Age" : 21 , "Male":True, "Adress": null,}'

Mydict = MyJSON.loads(JsonString)

print(Mydict)

print(type(Mydict))
print(Mydict["Name"])

print("----------------------------")

#try:
  # r = os.path.exists("JSON/TXT.JSON")

 #if r == True:
   # myfile = open("JSON/TXT.JSON", "r")


#except Exception as err:
#print("Error", str(err))