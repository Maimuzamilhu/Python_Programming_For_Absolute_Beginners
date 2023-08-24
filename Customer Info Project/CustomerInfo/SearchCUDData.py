CuID =input("Please Enter the Customer ID  to Search!")

FileName = "Info_"+CuID+".ptx"
print(FileName)

#for checking file exist or not

import os

R = os.path.exists(FileName)

if R  == True:
    
    f = open(FileName ,"r")
    CUD =f.read()
    f.close()
    print(CUD)

else:
    print("File do not exists")