#write a program to calculate the sum of "n" natural numbers
n=int(input("Enter a number: "))
s=(n*(n+1))/2
print("sum of first", n, "numbers is", s)

#using for loop
sum=0
for i in range(0,n+1):
    sum+=i
print(sum)