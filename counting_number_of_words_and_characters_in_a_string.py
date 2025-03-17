n=input("Enter a sentence: ")
c=0
w=0
for i in n:
    c+=1
    if i==" " or i=="." or i==",":
        w+=1
        c-=1
print(c, w)
    