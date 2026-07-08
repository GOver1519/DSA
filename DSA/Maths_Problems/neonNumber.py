n = int(input("Enter the number: "))
square = n**2
array = []
while square > 0:
    digit = square % 10
    array.append(digit)
    square = square // 10

add = 0
for i in array:
    add += i

if add == n:
    print("Neon number")
else:
    print("Not a neon number")
