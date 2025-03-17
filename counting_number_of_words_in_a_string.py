str=input("Enter a sentence:")
c=0
s=" "
for i in range(0,len(str)-1):
    if str[i] in " ,.:;":
        if str[i-1]==s:
            c=c
        if str[i+1]==s:
            c=c
        else:
            c+=1
print(c)