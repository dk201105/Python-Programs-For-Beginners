n=int(input("Enter number of elements:"))
l=[]
c=1
count=0
while c==1:
    for i in range(0,n):
        print("w")
        for j in range(2,(i//2)+1):
            print("W")
            if i%j==0:
                count=1
            else:
                l.append(j)
                print(l)
            
        count-=1
        if count == 1:
            print(i)
            
        