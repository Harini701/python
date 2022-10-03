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
    
print("Select your choice:\n"\
        "1.add\n"\
        "2.sub\n"\
        "3.mul\n"\
        "4.div\n"\
        "5.pow\n")
choice = int(input("Enter choice from 1,2,3,4,5: "))
X=int(input("Enter first value: "))
N=int(input("Enter second value: "))
if choice==1:
    print(X,"+",N,"=", add(X,N))
elif choice==2:
    print(X,"-",N,"=", sub(X,N))
elif choice==3:
    print(X,"*",N,"=", mul(X,N))
elif ((choice==4)and(N!=0)):
    print(X,"/",N,"=", div(X,N))
elif choice==5:
    print(X,"**",N,"=", pow(X,N))
else:
    print("Enter the valid choice")
    
