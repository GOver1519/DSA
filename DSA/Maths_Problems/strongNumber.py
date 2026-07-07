n = int(input("Enter the number: "))
sep = []
a = n
while a>0:
    digit = a % 10
    sep.append(digit)
    a = a // 10

factSum = 0
for i in sep:
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    factSum += factorial

if factSum == n:
    print("Strong number")
else:
    print("Not a strong number")

