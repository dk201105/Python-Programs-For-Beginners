def allowance(basic_pay):
    al=(20/100)*basic_pay
    monthly_income=basic_pay+al
    return monthly_income

def tax(monthly_income):
    if monthly_income < 5000:
        return 0
    elif monthly_income <10000:
        return monthly_income*(5/100)
    elif monthly_income <20000:
        return monthly_income*(10/100)
    else:
        return monthly_income*(15/100)
        

basic_pay=int(input("Enter Basic Pay:"))
al= allowance(basic_pay)
print("Monthly salary is: ", al)
tax= tax(al)
print("Tax is: ", tax)
total_income=al-tax
print("Total income is: ", total_income)


