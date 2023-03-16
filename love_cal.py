print("Welcome to love calculator")
Your_name = input("Enter Your name: ").lower()
partner_name = input("Enter Your partnar name: ").lower()
L = Your_name.count("l") + partner_name.count("l")
O = Your_name.count("o") + partner_name.count("o")
V = Your_name.count("v") + partner_name.count("v")
E = Your_name.count("e") + partner_name.count("e")
score_LOVE = L + O + V + E
T = Your_name.count("t") + partner_name.count("t")
R = Your_name.count("r") + partner_name.count("r")
U = Your_name.count("u") + partner_name.count("u")
E = Your_name.count("e") + partner_name.count("e")
score_TRUE = T + R + U + E
score = str(score_TRUE) + str(score_LOVE)
print(f"Your Love score is {int(score)}")
score = int(score)
if 10 >= score >= 90:
    print("You are not compatible")
elif 50 >= score >= 40:
    print("You are highly compatible")
else:
    print("You are less compatible")






