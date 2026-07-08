n = int(input("Enter the number: "))
a = n
array = []
while a>0:
    digit = a % 10
    array.append(digit)
    a = a // 10
add = 0
for i in array:
    add += i

if n % add == 0:
    print("Harshad number")
else:
    print("Not a Harshad number")
