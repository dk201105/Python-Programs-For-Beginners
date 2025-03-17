#function to find circle's circumference and area
import math 
def circle(r):
    a=math.pi*r**2
    c=2*math.pi*r
    return a,c
r=int(input("Enter Radius: "))
a=(area, circumference)=circle(r)
print("The area is", a[0], "The circumference is", a[1])