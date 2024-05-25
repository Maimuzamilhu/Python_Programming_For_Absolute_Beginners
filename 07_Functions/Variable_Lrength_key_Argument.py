def First_function(**Students):
    
    Myname =Students["Fname"]
    Myage = Students["Age"]

    print(f"Hi,{Myname}! You are {Myage} Years Old!")
    
First_function(Age = "21" , Fname = "Muzzamil")
First_function(Age = "32" , Fname = "AI")

