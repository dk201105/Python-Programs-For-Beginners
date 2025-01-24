#binary searching
import random
def create_list(n):
    l=[]
    for i in range(0,n):
        t=random.randint(1,100)
        l.append(t)
    '''for i in range(0,n):
        t=int(input("Enter marks:"))
        l.append(t)'''
    return l
def binary_search(a,x,low,high):
    pos=-1
    while(low<=high):
        mid=(low+high)//2
        if x==a[mid]:
            pos=mid
            break
        else:
            if x<a[mid]:
                high=mid-1
            else:
                low=mid+1
    if pos!=-1:
        print(x, "is present at position", pos+1, "in the sorted list\n")
    else:
        print(x, "is not present\n")

n=int(input("Enter number of terms:"))
arr=create_list(n)
print("The original list is:", arr, "\n")
low=0
high=len(arr)
x=int(input("Enter element to be found:"))
print()
arr1=sorted(arr)
print("The sorted list is:", arr1)
print()
b=binary_search(arr1, x, low, high)
for i in range(0, len(arr)):
    if x==arr[i]:
        print(x, "is in the position", i+1, "in the original list")
        break
            
            
            
    