try:
    age=int(input("Enter your age: "))
    if (age>=18):
        print("You can vote")
    elif(0<=age<18):
        print("You are allowed to vote after",18-age,"years")
    else:
        print("Age cannot be negative")

except ValueError:
        print("Enter a valid whole number")
    
    
