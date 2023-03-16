print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to T IERLAND")
print("Your main Aim is to find treaser I land")
decision_1 = input("You are at the cross road, Where do you want to go? Left or Right: ").lower()
if decision_1 == "left":
    print("")
    decision_2 = input("You are at the river front, What do you want to do? Wait or Swim: ").lower()
    if decision_2 == "wait":
        print("Great")
        decision_3 = input("You crossed the river now select the gate. Which gate do you want to select?"
                           " 'Red', 'Green' or 'Yellow': ").lower()
        if decision_3 == "yellow":
            print("Your decision is 'Yellow'. You got the 'Treasure'!.")
        elif decision_3 == "red":
            print("Your decision is 'Red'. You did not got the 'Treasure'!.")
            print("Game Over.")
        elif decision_3 == "green":
            print("Your decision is 'Green'. You did not got the 'Treasure'!.")
            print("Game Over.")
        else:
            print("Your decision is other than 'Red', 'Yellow', 'Green'. You did not got the 'Treasure'!.")
            print("Game Over.")
    elif decision_2 == "swim":
        print("Your decision is 'swim'.")
        print("Game Over.")
    else:
        print("Your decision is other than 'Wait' and 'Swim'.")
        print("Game Over")
elif decision_1 == "right":
    print("Your decision is 'Right'.")
    print("Game Over")
else:
    print("Your decision is other than 'Left' and 'Right'")
    print("Game Over")
