r = int(input("Enter the Total Number of Rows  : "))
c = int(input("Enter the Total Number of Columns  : "))

print("Rectangle Star Pattern") 
for i in range(r):
    for j in range(c):
        print('*', end = '')
    print()
