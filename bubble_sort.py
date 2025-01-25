#bubble_sort
a=[]
ele=int(input("Enter number of elements:"))
for i in range(ele):
    i=int(input("Enter number:"))
    a.append(i)
print("The unsorted array is:", a)
l=len(a)
for i in range(0,l-1):
    flag="sorted"
    for j in range(0,l-1):
        if a[j]>a[j+1]:
            a[j], a[j+1]= a[j+1], a[j]
            flag="not sorted"
    if flag=="sorted":
        break
print("The sorted array is", a)