n = int(input("Enter a number: "))

x = n + 1

i = 1
while i * i <= x:
    if i * i == x:
        print("Sunny Number")
        break
    i += 1
else:
    print("Not a Sunny Number")
