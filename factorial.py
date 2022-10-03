def factorial(n):
    fact = 1
    for i in range(2,n+1,1):
        fact*=i
    return fact
print("Enter the value of num: ")
num=int(input())
print("Factorial of",num,"is: ",factorial(num))
