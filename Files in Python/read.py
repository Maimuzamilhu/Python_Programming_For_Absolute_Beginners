MyFiles = open("Muzzamil.txt","rt")
#content = MyFiles.read(5) #inside ( ) we can write integer for example 5 then it will read only 5 characters!
#MyFiles.seek(10) # it will leave starting 10 letter the it start reading!

#Content = MyFiles.readline()
#print(content)
#Content = MyFiles.readline()
#print(content)
#Content = MyFiles.readline()

Content = MyFiles.readlines()
print(Content)

for x in Content:
    print(x.replace("\n",""))



MyFiles.close()