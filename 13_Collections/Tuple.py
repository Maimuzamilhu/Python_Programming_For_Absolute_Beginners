#tuple is like list but main difference is tuple is unchangeble and it is inside the() not in []

Mytuple =("Cat" , "Dog" , "lamb" ,"Goat")
Mynumber = (22,43,5555,322,55)
Mybools = (True,False,False,False,True)
Mystruct = (True , 22,"Goat",False)

#-------------Create tuple---------------

print(Mytuple)

#-------------tuple length---------------------------
print("----------------------------")

r = len(Mytuple)
print(r)

#------------------Read item---------------------------
print("----------------------------")

item =Mytuple[3]
print(item)

#-------------Slicing------------------------------
print("----------------------------")

item =Mytuple[0:3]
print(item)

#--------------Check if item exist or not--------------
print("----------------------------")

rr ="Dog" in Mytuple
#if rr == True:
    #print("Valid")
print(rr)

#--------------Packing and unpacking--------------
print("----------------------------")

(n1,n2,n3,n4) = Mytuple
print(n1,n2,n3,n4)

#--------------Multiply the tuple--------------
print("----------------------------")

Newtuple = Mytuple*3
print(Newtuple)

#--------------Joining two tuple--------------
print("----------------------------")

Newtuple = Mytuple+Mynumber
print(Newtuple)

