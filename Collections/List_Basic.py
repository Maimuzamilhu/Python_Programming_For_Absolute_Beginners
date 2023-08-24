Mylist = ["Cat" , "Dog" , "lamb" ,"Goat"]
Mynumber = [22,43,5555,322,55]
Mybools = [True,False,False,False,True]
Mystruct = [True , 22,"Goat",False]

#================================================
print("==========================================")
print(Mylist)
print(Mybools)
print(Mynumber)
print(Mystruct)
#================List or length ==================
print("============================================")

Items = len(Mylist)
print(Items)

#====================Read Items==============================
print("====================================================")

item = Mylist[1] #index sy read
print(item)

#========Change item ============================================
print("=======================================================")

Mylist[2] = "india"
print(Mylist) 

#=============Append(add)item
print("=====================================================")

Mylist.append("gK")
print(Mylist)

#===============Insert Items==============================
print("======================================================")
Mylist.insert(2 ,"Insta")
print(Mylist)
#==================Remove==========================
print("=============================================")

Mylist.remove("Goat")
print(Mylist)
#==============Clear the list==================
print("=====================================")
Mylist.clear()
print(Mylist)












