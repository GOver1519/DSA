num = int(input("Enter a number: "))

digits = len(str(num))
square = num * num

right = square % (10 ** digits)
left = square // (10 ** digits)

if left + right == num:
    print("Kaprekar Number")
else:
    print("Not a Kaprekar Number")
