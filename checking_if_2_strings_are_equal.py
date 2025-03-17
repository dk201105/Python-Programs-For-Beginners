#checking whether 2 strings are equal or not
w1=input("Enter string 1:")
w2=input("Enter string 2:")
c=0
for i in range(0,len(w1)):
    if w1[i]==w2[i]:
        c+=1
if c==len(w1):
    print("\nThe strings",w1,"&", w2,"are equal")
else:
    print("\nThe strings",w1,"&", w2,"are not equal")
    
        

