str=input("Enter string:")
v=0
c=0
for i in str:
    if i in "aeiouAEIOU":
        v+=1
    else:
        c+=1
print("Number of vowels:", v, "\nNumber of consonants:", c)
        