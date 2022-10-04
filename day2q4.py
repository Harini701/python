[10:56 am, 04/10/2022] Dhanalakshmi SSE: def count_chars(str):
    u,l,n,s=0,0,0,0
    for i in range(len(str)):
        if str[i]>='A' and str[i]<='Z': u+=1
        elif str[i]>='a' and str[i]<='z': l+=1
        elif str[i]>='0' and str[i]<='9': n+=1
        else: s+=1
    return u,l,n,s

str=input("enter any substring=")
u,l,n,s=count_chars(str)
print("\n upper case charecters are:",u)
print("lower case charecters are:",l)
print("number case:",n)
print("special case charecters:",s)
[10:56 am, 04/10/2022] Dhanalakshmi SSE: try:
    num = int(input("Enter the number:"))
    reversed_num = 0

    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
        
    print("Mirror image: " + str(reversed_num))

except ValueError:
    print("no special cahrectors allowed raju only number are allowed
