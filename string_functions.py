#string functions
str="this is a sentence. The sentence ends with a fullstop, The sign before this sentence is a comma."
print("This is the string:",str)
#capitalize function
cap=str.capitalize()
print("\nThe captilized version is:",cap)
#center
cen=str.center(len(str)+30,"#")
print("\nThe centered version is:",cen)
#count
c=str.count("sentence")
print("\nThe count of the word sentence is:",c)
#ends with
ew=str.endswith(".")
print("\nEnds with '.'?",ew)
#starts with
sw=str.startswith("T")
print("\nStarts with 'T'?",sw)
#find
fi=str.find("the")
print("\nThe index at which the word 'the' appears is:",fi)
#isalpha
al=str.isalpha()
print("\nThe string contains only alphabets?",al)
#isascii
asc=str.isascii()
print("\nThe string contains only ascii characters?",asc)
#isalnum
an=str.isalnum()
print("\nThe string contains only alphabets and numbers?",an)
#islower
lo=str.islower()
print("\nThe string contains only lower case?",lo)
#isnumeric
al=str.isnumeric()
print("\nThe string contains only numbers?",al)
#isupper
up=str.isupper()
print("\nThe string contains only upper case?",up)
#length
l=len(str)
print("\nThe length of the string is:",l)
