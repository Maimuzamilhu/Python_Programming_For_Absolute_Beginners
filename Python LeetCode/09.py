""" Bisection Method
step 01 ---Function create
step02 --- a: 1st Approximate root
step03 --- b: 2nd Approximate root
step04 --- n : No of iteration
step05 --- if f(a).f(b)>0 ===then do not have bracker root
step06 ---x =(a+b)/2


step 07 ---- if f(x)<0 : a=x 
                else b = x
step 08 ----- Require Root
End


f(x) = X*3 - 5x +1 = 0
"""
def f(x):
    return x - 2*-x + 1

def bisection(a, b, n):
    i = 1
    while i <= n:
        x = (a + b) / 2
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        print("Iteration =", i, "x =", x, "f(x) =", f(x))
        i = i + 1

    print("Required Root is:", x)


    print("Required Root is :" , x)


a = float(input("First Approximation Root :"))
b = float(input("Second Approximation Root :"))

n = int(input("Number of Iterations :"))

if f(a)*f(b)>0:
    print("Given approximate root does not bracket the root:")
    print("Try again with Different Values...")

else:
    bisection(a , b , n)