def vowels(s):
  count = 0
  s=s.lower()
  for i in s:
     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count+=1

  if count == 0:
    print('No vowels found')
  else:
    print('Total vowels are :' + str(count))

s= input('Enter the string :')
vowels(s)
