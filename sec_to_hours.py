s=int(input("Enter time in seconds: "))
h=s//(60*60)
m=s%60
S=0
if m>60:
    
print(h,"Hours",m,"Minutes", S,"Seconds")