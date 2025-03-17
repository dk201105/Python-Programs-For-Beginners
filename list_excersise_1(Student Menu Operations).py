#create a list of student names and do the following functions 1) Add Student names 2) Delete Student Namw 3) Check whether the student's name is in the list 4) End 

l=[ ]
choice="n"
while choice=="n":
    n=int(input("Type the Item number needed\n1. Create a List\n2.Add a Student's Name\n3.Delete a Student's Name\n4.End"))
    print()
    if n==1:
        num=int(input("Enter number of Students:"))
        print()
        for i in range(0,num):
            name=input("Enter Student Name: ")
            print()
            l.append(name)
            print(l)
            print()
        choice=input("Do you want to end the program (y/n): ")
        print()
            
    elif n==2:
        name=input("Enter Student Name: ")
        print()
        l.append(name)
        print(l)
        print()
        choice=input("Do you want to end the program (y/n): ")
        print()
        
    elif n==3:
        name=input("Enter Student Name: ")
        print()
        if name not in l:
            print("This element is not in l")
            print()
            print(l)
            print()
        l.remove(name)
        choice=input("Do you want to end the program (y/n): ")
        print()
        
    elif n==4:
        choice=input("Do you want to end the program (y/n): ")
        print()
        choice1=choice.lower()
        if choice1=="n":
            n=int(input("Type the Item number needed\n1. Create a List\n2.Add a Student's Name\n3.Delete a Student's Name\n4.End\n"))
            print()
            choice="y"
        else:
            break
    