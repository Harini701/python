def users(t,s):
        if(t>0 and s>0 and t>s):     
          nt=s//3
          stu=t-(s+nt)
          print("STUDENT USERS=",stu)
        elif(t>0 and s>0 and t<s):
          print("TOTAL USERS CANNOT BE LESSER THAN STAFF USERS")
        elif(t>0 and s>0 and t==s):
          print("TOTAL USERS CANNOT BE EQUAL TO STAFF USERS")   
        elif(t==0 or s==0):
          print("VALUE CANNOT BE ZERO")
        else:
          print("NEGATIVE")

t=int(input("TOTAL USERS="))
s=int(input("STAFF USERS="))
users(t,s)
