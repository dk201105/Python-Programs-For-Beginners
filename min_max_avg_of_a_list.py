#to find the minimun, maximum and avg of a list
import random
l=[]
for i in range(0,12):
    t=random.randint(1,100)
    l.append(t)
print(l)
min=100
max=0
for i in l:
    if i<min:
        min=i
print("The minimum value is:", min)
for i in l:
    if i>max:
        max=i
print("The maximum value is:", max)
sum=0
for i in l:
    sum+=i
avg=sum/2
print("The average is:", avg)
