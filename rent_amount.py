'''A video library rents new videos for 75$ a day and old movies for 
$50 a day. WAP to calculate the total charge for a customers video 
rentals the program should prompt a user for the number of each type
 of video and output the total cost, how many days per video'''
new= 75
old= 50
o1=int(input("Enter number of old videos rented: "))
o2=int(input("Enter number of days old videos were rented: "))
n1=int(input("Enter number of new videos rented: "))
n2=int(input("Enter number of days new videos were rented: "))
total= (old*o1*o2)+(new*n1*n2)
print(total, "rupees to be paid")