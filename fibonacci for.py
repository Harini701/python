def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n,1):
            c=a+b
            a=b
            b=c
            print(c)
print("Enter the value of num: ")
num=int(input())
fib(num)
