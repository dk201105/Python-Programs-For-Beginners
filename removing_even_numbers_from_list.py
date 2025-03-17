l=[]
l1=[]
n=int(input("Enter number of elements:"))

for i in range(0,n):
    ele=int(input("Enter element"))
    l.append(ele)
print(l)

for i in l:
    if i%2==0:
        l1.append(i)
        
for i in l1:
    if i in l:
        l.remove(i)
        
print(l)