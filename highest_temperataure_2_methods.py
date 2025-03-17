a=0
n=int(input("Enter number"))
for i in range(0,n):
    temp=int(input("Enter temperature: "))
    if temp>a:
        a=temp
'''for i in range(0, len(l)-1):'''
    if l[i]>a:
        a=l[i]
print("The highest temperature is", a)