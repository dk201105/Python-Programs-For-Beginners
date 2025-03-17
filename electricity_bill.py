#electricity bill reading
pr=int(input("Enter previous reading: "))
cr=int(input("Enter current reading: "))
uni=cr-pr
print("Number of units used: ", uni)
if uni<100:
    print("The amount to pay is", (uni*0.85)+50)
elif uni<500:
    print("The amount to pay is", (uni*1.25)+75)
elif uni<1000:
    print("The amount to pay is", (uni*1.50)+125)
else:
    print("The amount to pay is", (uni*2)+200)