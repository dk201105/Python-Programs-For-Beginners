str=input("Enter a string:")
l=len(str)-1
str2=""
for i in range(l,-1,-1):
    str2+=str[i]
print(str2)