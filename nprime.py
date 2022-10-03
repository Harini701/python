N=int(input("Enter the number: "))
x=1
c=0
while(c<N):
      x+=1
      for i in range(2,x+1):
          if(x%i==0):
              break
      if(i==x):
          c=c+1
print(n,"th ","prime number is ",x)
for n in range(x,N):
            for i in range(2,n):
                  if(n%i==0):
                        break
            else:
                  print(n,end=' ')
