import random
rand_seed = int(input("Enter the seed number: "))
random.seed(rand_seed)
random_int = random.randint(1, 10)  # include 1  and 10
print(f"The random integer number is {random_int}")
random_float = random.random()  # exclude 0  and 1
print(f"The random float number is {random_float}")
print(f"The random float number is {random_float*5}")   # exclude 0  and 5
coin_side = random.randint(0, 1)
if coin_side == 0:
    print("HEAD")
else:
    print("TAILS")
names = input("Enter the names seperated by coma: ")
names_List = names.split(",")
print(names_List[random.randint(0, len(names_List)-1)])
choise = random.choice(names_List)
print(choise)
print(names_List.index(choise))  # list.index(index_variable)


