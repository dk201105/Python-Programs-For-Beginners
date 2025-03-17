#counting number of students who passed
#for loop
n=int(input("Enter number of students: "))
c=0
for i in range(1,n+1):
    mark=int(input("Enter mark of student:"))
    if mark>=50:
        print("The student has passed")
        c+=1
    else:
        print("the student has failed")
print("The number of students who passed the exam are ",c)

#while loop
n=int(input("Number of marks to be processed: "))
c=0
i=0
while(i<n):
    mark=int(input("Enter mark: "))
    if mark>=50:
        c+=1
        print("pass")
    else:
        print("fail")
    i+=1
print("Number of students who passed are: ", c)
