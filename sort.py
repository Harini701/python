def sort(S):
    Word=S.split(" ")
    for i in range(len(Word)):
        Word[i]=Word[i].lower()
    Word.sort()
    return Word
string=input("Enter the string: ")
print(sort(string))
