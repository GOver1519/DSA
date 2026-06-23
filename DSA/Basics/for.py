low = int(input("Enter the lowest number: "))
high = int(input("Enter the highest number: "))

result = 0

for i in range(low, high+1):
    result += i
    
print(result)