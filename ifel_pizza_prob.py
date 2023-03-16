print("Welcom Pizza Shop")
size = input("Enter your pizza size 'L' 'M' 'S' ")
add_peproni = input(" Do you want add peperoni 'Y' or 'N'")
add_extra_chise = input("DO you wanted add extra chise 'Y' or 'N': ")
bill = 0
if size == "L":
    bill = 400
elif size == "M":
    bill = 300
elif size == "S":
    bill = 200
else:
    print("Please enter the correct size ! re run the program")
if add_peproni == "Y":
    if size == "S":
        bill += 20
    else:
        bill += 25
if add_extra_chise == "Y":
    bill += 50
print(f"Your pizza bill is {bill} ruppes")
