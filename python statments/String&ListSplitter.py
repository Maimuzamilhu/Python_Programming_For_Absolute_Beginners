A = input("Enter the Sentence! :")
length = len(A)
indexlist = range(0,length)

for index in indexlist:
    r = A[index]
    print(f"{index}:{r}")
