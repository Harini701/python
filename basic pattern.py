r=int(input("Enter the number of rows: "))
k=2*r-2
for i in range(1,r):
    for j in range(k,1,-1):
        print(end=" ")
    k=k-1
    for j in range(1,i+1):
        print(i,end=" ")
    print("\r")
