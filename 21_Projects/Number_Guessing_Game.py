CurrentTry = 1
TotalChances = 3
CorrectAnswer = 6

while CurrentTry <= TotalChances:
    User_Answer = input("Enter Your Guesses (Between 0 to 9): ")
    CurrentTry += 1
    User_Answer = User_Answer.replace(" ","")
    if User_Answer == "":
        print("Please Enter Valid Number :")
        continue

    User_Answer = int(User_Answer)  # Convert user input to an integer
    CurrentTry += 1

    if User_Answer == CorrectAnswer:
        print("You won bro!")
        break
    else:
        print(f"Wrong Answer : Try Again! Left ({TotalChances-CurrentTry} out of {TotalChances})")

        CurrentTry+=1
    
else:
 
 
        print("You lost")
