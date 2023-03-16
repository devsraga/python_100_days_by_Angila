import random as rand
import hang_man_ascii as art
import hangman_words as hw

hangman = art.hangman
hangman_art_1 = art.hangman_logo_1
hangman_art_2 = art.hangman_logo_2
print(hangman_art_1)
print(hangman_art_2)
words = hw.hangman_words_collection
sys_choice = rand.choice(words)
choice_len = len(sys_choice)
dash = []
for ind in range(choice_len):
    dash += "_"
print(dash)
end_of_the_game = False
n = 0
while not end_of_the_game:
    user_choice = input("Please enter the one small case letter from the alphabet:\n").lower()
    if user_choice in dash:
        print("The chosen letter is already in the list")
    for check in range(choice_len):
        if sys_choice[check] == user_choice:
            dash[check] = user_choice  # changing a index element only
    print(dash)
    print(hangman[n])
    if user_choice not in dash:
        print("user choice is not in this word")
    n += 1
    if n > len(hangman) - 1:
        end_of_the_game = True
        print(" 'Game Over' bcz you not saved to hang man")
    elif '_' not in dash:

        end_of_the_game = True
        if n < len(hangman):
            print("########################################")
            print("You won the game bcz you save hang man")
            print("JEET GAE !!")
            print("########################################")
