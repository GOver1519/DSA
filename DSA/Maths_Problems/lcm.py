n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))

n1Factors = []
n2Factors = []

gcd = 0
for i in range(1, n1+1):
    if n1 % i == 0:
        n1Factors.append(i)
for j in range(1, n2+1):
    if n2 % j == 0:
        n2Factors.append(j)

for k in n2Factors:
    if k in n1Factors and k > gcd:
        gcd = k
print("LCM = ",(n1*n2)//gcd)
