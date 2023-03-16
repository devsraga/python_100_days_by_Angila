print("HI Welcome to Leap Year finder")
year = int(input("Enter the year which you want to check Leap Year: "))
print(f"You enter the year {year}")
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("This year is Leap year")
        else:
            print("This year is not leap year")
    else:
        print("This is a Leap Year")
else:
    print("This is not a Leap Year")

