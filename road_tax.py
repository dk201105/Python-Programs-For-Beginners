amt=int(input("Enter the price of the bike:"))
if amt>100000:
    tax=(15/100)*amt
    print(tax,"rupees to be paid")
elif amt>50000:
    tax=(10/100)*amt
    print(tax,"rupees to be paid")
else:
    print("No tax to be paid")
