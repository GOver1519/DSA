n = int(input("Enter the number: "))
a = n
reverse = 0
while a>0:
    digit = a % 10
    reverse = reverse*10 + digit
    a = a // 10
    
if reverse == n:
    print("Palindrome")
else:
    print("Not a palindrome")
