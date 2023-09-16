Mylist = ["Cat" , "Dog" , "lamb" ,"Goat"]
Mynumber = [22,43,5555,322,55]
Mybools = [True,False,False,False,True]
Mystruct = [True , 22,"Goat",False]

#========Slicing==========
r = Mylist[:2]
#r = Mylist[-2:]
print(r)

#=====Check if its exists or not====================
print("=============================================")

rr ="Goat" in Mylist
#if rr == True:
    #print("Valid")
print(rr)

#===============Loops through a List=====================
print("=============================================")

for x in Mylist:
    print(x)

#=======Sort a List======================= 
print("========================================")
#it will convert in decending order
Mylist.sort(reverse=True)
print(Mylist)

#==========reverse =======================
print("=====================================")

Mylist.reverse()
print(Mylist)

#===============Copy a List ========================
print("=============================================")

newlist=Mylist.copy()
print(newlist)

#==================Extent the list======================================
print("===========================================")

Mylist.extend(Mynumber)
print(Mylist)

#=======================Join two list========================================
print("====================================================================")

for item in Mynumber:
    Mylist.append(item)
    print(Mylist)