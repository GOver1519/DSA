n = int(input("Enter the number: "))
power = int(input("Enter the power: "))
sol = 1
for i in range(power):
    sol *= n
print(sol)
