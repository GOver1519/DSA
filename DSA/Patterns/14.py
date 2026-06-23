rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        if i == j or i == rows or j == 1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()