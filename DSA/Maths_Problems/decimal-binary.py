n = int(input("Enter the number: "))
binary_str = ""
while n > 0:
    remainder = n % 2       
    binary_str = str(remainder) + binary_str  
    n = n // 2 
print(binary_str)
