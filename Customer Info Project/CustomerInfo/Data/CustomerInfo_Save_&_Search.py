CuID =input("Please Enter the Customer ID!")
CuName =input("Please Enter the Customer Name!")
CuGender =input("Please Enter the Customer Gender!")
CuCell =input("Please Enter the Customer Cell!")


FileName = "Info_"+CuID+".ptx"

Cudata = f"Id = {CuID}\nName = {CuName}\nGender = {CuGender}\nCell = {CuCell}"
print(Cudata)

File = open(FileName ,"w")
File.write(Cudata)

File.close()