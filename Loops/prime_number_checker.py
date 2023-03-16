def prime_checker(number):
    try:
        if '.' not in number:
            num = int(number)
            if num == 1:
                print(f"The number {num} is not a prime number.")
            else:
                flag = 0
                for ind in range(2, num):
                    if num % ind == 0:
                        flag = 1
                if flag != 1:
                    print(f"The number {num} is a prime number.")
                else:
                    print(f"The number {num} is not a prime number.")
        else:
            print(f"The number {number} is a float number please enter an integer number.")
    except:
        print("Please enter integer only. Your input argument is other than integer such as string, bool etc.")


num = input("Enter an integer number to check prime number or not: ")
prime_checker(number=num)

