# functions without input and output
def my_function():
    name = input("Please enter your name\n")
    print(f"Your name is:\n{name}")
    print(f"Your name has length: {len(name)}")
    list_of_words = name.split()
    print(f"Your name has total {len(list_of_words)} words")


def greet():
    print("hello !")
    print("How are you ?")
    print(input("Is whether is fine ?: "))
    print('ok !')


# functions with input and without output
def greet_with_name(name):  # name(parameter) = dev(argument)
    print(f"hello {name} !")
    print("How are you ?")
    print(input("Is whether is fine ?: "))
    print('ok !')


def greet_with_name_location(name, location):  # name(parameter) = dev(argument)
    print(f"hello {name} !")
    print("How are you ?")
    input(f"Is whether is fine in {location}?: ")
    print('ok !')


# functions with output
# ----------------------------------
my_function()
greet()
greet_with_name("Dev Kunwar Singh Chauhan")
greet_with_name_location("Dev", "Jatani")
greet_with_name_location(location="jatani", name="dev")  # is same as above even change the order of the argument

