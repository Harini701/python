try:
    num = int(input(" Enter the number: "))
    Sum = 0
    if(num>=0):
        for i in range(1, num,1):
            if(num % i == 0):
                Sum = Sum + i
        if (Sum == num):
            print(num, "is a Perfect Number")
        else:
            print(num,"is not a Perfect Number")
    else:
        print("Enter a positive integer")
        
except ValueError:
        print("Enter a valid whole number")
