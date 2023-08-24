def recursion(n):
    print(n)
    if n == 0:
        return
    else:
        n = recursion(n-1)
    recursion(5)