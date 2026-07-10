n = int(input("Enter a number: "))
a = n
digits = []
while a  > 0:
    digits.append(a % 10)
    a = a // 10

digits.reverse()
sum = 0
for i in range(len(digits)):
    sum += digits[i] ** (i+1)

if sum == n:
    print("Disarium number")
else:
    print("Not a disarium number")
