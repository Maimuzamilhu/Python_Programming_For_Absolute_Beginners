#continue is used fr to remove number

A = input("Enter the number:")
B = input("Which number you want to remove :")

A = int(A)
B = int(B)


while A <= 100:

    A =A+1
    if A == B:
        continue
