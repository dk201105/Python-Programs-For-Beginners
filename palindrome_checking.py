#palindrom checking
text=input("Enter word: ")
c=0
j=-1
for i in range(0,len(text)):
    if text[j]==text[i]:
        c+=1
    j+=-1
if c==len(text):
    print("This is a palindrome")
else:
    print("This is not a palindrom")
    
    

