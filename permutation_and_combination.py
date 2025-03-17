#permutation and combination
n=int(input("Enter n: "))
r=int(input("Enter r: "))
nr=n-r
f1=1
f2=1
f3=1
for i in range(1,n+1):
    f1*=i   #n!
for j in range(1,r+1):
    f2*=i   #r!
for k in range(1,nr+1):
    f3*=i   #(n-r)!
    
p=f1/f3
c=f1/(f2*f3)

print("Permutation:", p, "Combination:", c)
    
    