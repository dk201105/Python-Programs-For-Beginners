#linear search
l=[]
def list_create(n):
    for i in range(0,n):
        name=input("Enter name:")
        l.append(name)
    print("The list of names are:", l,"\n")
    return l
    
def linear_search(l, tn):
    flag=0
    for i in range(len(l)):
        if tn.lower().strip()==l[i]:
            flag+=1
            break
    if flag!=0:
        print("The name", tn, "is found in this list and it's position is", i+1)
    else:
        print("The name", tn, "is not in list")
    
n=int(input("Enter number of names:"))
l=list_create(n)     
tn=input("Enter name you want to search for: ")
s=linear_search(l,tn)                                                   