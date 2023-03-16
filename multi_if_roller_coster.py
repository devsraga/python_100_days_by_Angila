print("Welcome to Roller Costar Ride")
name = input("Enter your name: ")
weight = float(input("Enter the total weight of your body in kilograms: "))
height = float(input("Enter your height in meters: "))
age = float(input("Enter your age in years: "))
print("Thank you " + name)
bill = 0
if height >= 1.2:
    print("You can ride the Roller Costar")
    if age < 12:
        bill = 5
    elif 18 >= age >= 12:
        bill = 7
    else:
        bill = 11
    photo = input("Do you wanted to take photo, if Yes press 'Y' else 'N': ")
    if photo == "Y":
        bill += 3
    print(f"Your bill is {bill} rupees")
else:
    print(f"Your height is {height} meter You can not ride the Roller Costar")
