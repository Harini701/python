year=int(input("Enter any year: "))

if(year%400==0):
    print(year,"is an leap year.")
elif(year%4==0):
    print(year,"is an leap year.")
elif(year%1==0):
    print(year,"is not an leap year.")
else:
    print(year,"is not an leap year.")
    
