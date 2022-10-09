def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def pow(a,b):
    return a**b

print("Select operator: ")
print("1.+")
print("2.-")
print("3.x")
print("4./")
print("5.^")

while True:
    choice = input("Enter the choice(1/2/3/4/5) : ")

    if (choice in ('1','2','3','4','5')):
        a=float(input("Enter first number: "))
        b=float(input("Enter second number: "))

        if(choice=="1"):
           print(a,"+",b,"=",add(a,b))
        elif(choice=="2"):
           print(a,"-",b,"=",sub(a,b))
        elif(choice=="3"):
           print(a,"x",b,"=",mul(a,b))
        elif(choice=="4")and(b!=0):
           print(a,"/",b,"=",div(a,b))
        elif(choice=="5"):
            print(a,"^",b,"=",pow(a,b))
        else:
            print("Entries invalid")

        next_cal=input("lets do next calculation?(yes/no):")
        if(next_cal=="no"):
            break
    else:
        print("Invalid Input")
