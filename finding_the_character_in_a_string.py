#finding whether a character is in a string or not
s="asdjsahdjkhsajkdhjksahdjkhskdjhsjkd"
c=input("Enter character to find: ")
for i in range(0, len(s)):
    if c==s[i]:
        print("The character is in the string and is in the", i+1, "postition")