import random
def create_list(n):
    l=[]
    for i in range(n):
        t=random.randint(1,100)
        l.append(t)
    return l
def partition(a,x):
    i=0
    j=len(a)-1
    while(a[i]<=x and i<j):
        i+=1
    while(x<a[j] and i<j):
        j-=1
    while(i<j):
        a[i], a[j] = a[j], a[i]
        print(i, j, "array=", a)
        i=i+1
        j=j-1
        while(a[i]<=x and i<j):
            i+=1
        while(a[j]>x and i<j):
            j=j-1
    p=j
    print("p:", a[p])
    print("partitioned array: ", a)

ans="y"
n=int(input('Enter number of elements:'))
arr=create_list(n)
while ans=="y":
    print("original array is: ",arr)
    t=int(input("Pivot="))
    partition(arr, t)
    ans=input("Do you want to continue (y/n)")
    

        
    
