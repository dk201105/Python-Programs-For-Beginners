def writing():
    f=open("txt.txt", "w")
    i=input("Enter words to be written: ")
    f.write(i)
    f.close()

def reading():
    text= open("txt.txt", "r")
    n=text.read()
    tab=0
    space=0
    n1=0
    wc=0
    for char in n:
        if char == "\t":
            tab+=1
        elif char == " ": 
            space+=1
        elif char == "\n":
            n1+=1
        elif char.isalpha():
            wc+=1
    
    
    print("TABS= ", tab)
    print("SPACE= ", space)
    print("NEW LINE= ", n1)
    print("LETTER COUNT= ", wc)

    text.close()

def appending():
    f=open("txt.txt", "a")
    i=input("Enter words to be appended: ")
    f.write(i)
    f.close()
    
def cont():
    con=input("Do you want to continue? (y/n)")
    if con=="y":
        option()

def option():
    option=int(input("Enter an option- Read(1), Write(2), Append(3)"))
    if option == 1:
        reading()
        cont()
    elif option == 2:
        writing()
        cont()
    elif option == 3:
        appending()
        cont()

option()