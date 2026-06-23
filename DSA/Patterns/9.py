n = 3
for upperRow in range(n):
    for upperSpace in range(0, (n-upperRow-1)):
        print(" ", end = "")
    for upperColumn in range(0, 2*upperRow+1):
        print("*", end = " ")
    print()
for lowerRow in range(n):
    for lowerSpace in range(0, lowerRow):
        print(" ", end = "")
    for lowerColumn in range(0, 2*n - (2*lowerRow+1)):
        print("*", end = " ")
    print()