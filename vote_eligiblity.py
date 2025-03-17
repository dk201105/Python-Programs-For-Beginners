#age eligibily vote
age=int(input("Enter Age: "))
if age>=18:
    print("They are eligible to vote!")
else:
    n=18-age
    print("They are not eligible to vote, they have ", n, "years to vote")
