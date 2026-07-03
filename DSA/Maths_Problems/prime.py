n = int(input("Enter the number: "))
if n <= 1:
    isPrime = False
else:
    isPrime = True
    
    for i in range(2, n):
        if n % i == 0:
            isPrime = False
            break
print(isPrime)



