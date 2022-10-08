def findReverse(n): 
   reverse = ''
   for i in range(len(n), 0, -1):
      reverse += n[i-1]
   return reverse
num = input('Enter the number: ')
reverse = findReverse(num)
print('The reverse number is =', reverse)
