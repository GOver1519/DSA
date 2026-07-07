n = int(input("Enter the number: "))
square = n ** 2

narray = []
while n>0:
    digit = n % 10
    narray.append(digit)
    n = n // 10
squareArray = []
while square>0:
    digit = square % 10
    squareArray.append(digit)
    square = square // 10
if narray == squareArray[0:len(narray)]:
    print("Automorphic number")
else:
    print("Not an Automorphic number")

