n = int(input("Enter the number: "))
fibonacci = [0, 1]
for i in range(n-2):
    fibonacci.append(fibonacci[i] + fibonacci[i+1])
print(fibonacci)
