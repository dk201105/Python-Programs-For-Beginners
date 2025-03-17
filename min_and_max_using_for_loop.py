n = int(input("Enter the number of terms to be compared: "))

if n > 0:
    num = int(input("Enter number: "))
    min_num = max_num = num

    for i in range(1, n):
        num = int(input("Enter a number: "))
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    print("Max number is:", max_num )
    print("Min number is:", min_num)
else:
    print("Please enter a valid number of terms.")

