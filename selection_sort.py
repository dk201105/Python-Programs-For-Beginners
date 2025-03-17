import random
a=[]
l=random.randint(10,25)
for i in range(0, l):
    t=random.randint(0,100)
    a.append(t)
print(a)
for i in range(0,l-1):
    min=a[i]
    pos=i
    for j in range(i+1, l):
        if a[j]>min:
            min=a[j]
            pos=j
        a[pos], a[j] = a[j], a[pos]
print(a)
    

