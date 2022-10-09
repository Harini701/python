a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
n = 0
 
for i in range(1, min(a, b)+1):
    if a%i==b%i==0:
        n+=1
     
print(n)
