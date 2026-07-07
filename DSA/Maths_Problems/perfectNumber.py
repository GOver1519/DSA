n = int(input("Enter the number: "))
factors = []
for i in range(1, n):
    if n%i == 0:
        factors.append(i)
sum = 0
i = 0
while i<len(factors):
    sum += factors[i]
    i += 1
if sum == n:
    print("Perfecr number")
else:
    print("Not a perfect number")
