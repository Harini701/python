try:
    n=int(input("Enter the number to be reversed: "))
    org=n
    sum=0
    while(n>0):
        a=n%10
        sum=sum*10+a
        n=n//10
        print(a)
except ValueError:
    print("Enter only numbers")
