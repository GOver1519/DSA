n = int(input("Enter the number: "))
a = n

visited = []

while a != 1 and a not in visited:
    visited.append(a)

    array = []

    while a > 0:
        digit = a % 10
        array.append(digit)
        a = a // 10

    sum = 0
    for i in array:
        sum += i ** 2

    a = sum

if a == 1:
    print("Happy Number")
else:
    print("Not Happy Number")
