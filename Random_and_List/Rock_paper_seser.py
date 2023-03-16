print("Welcome to Rock Paper Scissor")
import random

user = int(input("Enter the choice for 'Rock', 'Paper', 'Scissor' as '0', '1', '2':  "))
if user == 0:
    print('''"!!!THAT'S IT, MAN!!! KEEP THROWING THAT
HEAVY SHIT AT ME!!! THAT HEAVY SHIT!!!"   _____
        \                              /\| | | |
         \                            / /|_|_|_|
          \                           \        |
            (  ( ) ) ( )  )            \_______/
           ( ( ( ( )  )  ) )           /______/
          ( ( )) ) (   ) ( ( )        /       /
          ( (__.-.___.-.__) )        /       /
          / ---._.---._.---\        /       /
          \||    '/  '   ||/       /       /
            |||  (_     |||       /       /
             || ///\\\  ||\______/       /
        ___/ ||||\__/|||||/             /
       /   \   ||||||||  /             /
      /     \   ||||||  /        _____/
jro
''')
    print("Your choice is 'Rock'")
elif user == 1:
    print('''
_ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|        ''')
    print("Your choice is 'Paper'")
elif user == 2:
    print('''                                                                    
                     88                                             
                     ""                                             
                                                                    
,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba,  
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8  
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88          
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88          
                                                                    
                                                                    ''')
    print("Your choice is 'Scissor'")
else:
    print("You chose wrong value. Rerun the program")
computer = random.randint(0, 2)
if computer == 0:
    print('''"!!!THAT'S IT, MAN!!! KEEP THROWING THAT
HEAVY SHIT AT ME!!! THAT HEAVY SHIT!!!"   _____
        \                              /\| | | |
         \                            / /|_|_|_|
          \                           \        |
            (  ( ) ) ( )  )            \_______/
           ( ( ( ( )  )  ) )           /______/
          ( ( )) ) (   ) ( ( )        /       /
          ( (__.-.___.-.__) )        /       /
          / ---._.---._.---\        /       /
          \||    '/  '   ||/       /       /
            |||  (_     |||       /       /
             || ///\\\  ||\______/       /
        ___/ ||||\__/|||||/             /
       /   \   ||||||||  /             /
      /     \   ||||||  /        _____/
jro
''')
    print("Computer's choice is 'Rock'")
elif computer == 1:
    print('''
_ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|        ''')
    print("Computer's choice is 'Paper'")
elif computer == 2:
    print('''                                                                    
                     88                                             
                     ""                                             

,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba,  
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8  
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88          
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88          

                                                                    ''')
    print("Computers choice is 'Scissor'")
else:
    print("You chose wrong value. Rerun the program")


if user == 0 and computer == 1:
    print("You lose")
elif user == 0 and computer == 2:
    print("You Win")
elif user == 1 and computer == 0:
    print("You Wins")
elif user == 1 and computer == 2:
    print("You lose")
elif user == 2 and computer == 0:
    print("You lose")
elif user == 2 and computer == 1:
    print("You win")
elif user == computer:
    print("Both win try again")
else:
    print("try again")

