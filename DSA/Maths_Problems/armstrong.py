n = int(input("Enter the number: "))
a = n
digits = len(str(n))
power = 0

while a > 0:
    digit = a % 10
    power += digit ** digits
    a = a // 10
if power == n:
    print("Is armstrong")
else:
    print("Not an armstrong")



