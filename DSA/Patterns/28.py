n = 5
for i in range(n):
    num = 1
    for j in range(n - i):
        print(" ",end = " ")
    for k in range(i+1):
        print(num, end = "   ")
        num = num * (i-k) // (k+1)
    print()
