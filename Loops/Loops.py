my_friends = ["Pooja", "Dev", "maggi", "rock"]  # this is a list which is not integer
print(my_friends)
for name in my_friends:
    print(name + " hai")

heights = input("Enter the students height with coma: ").split(",")    # Split is use to make a list after seperating by coma
print(heights)
print(type(heights))
sum_of_heights = 0
number_of_students = 0
b = 0
for height in heights:         # choosing from a list, don't forget : in for loop
    sum_of_heights += int(height)     # converting list item in integer because list elements are in string
    number_of_students += 1
    a = int(height)
    if a > b:
        b = a
    else:
        b = b
print(b)
print(sum_of_heights)
print(number_of_students)
avrage_height = sum_of_heights/number_of_students
print(avrage_height)
sum_num = 0
x_sum = 1
for num in range(0,101,2):  # range(from, till, difference)
    print(num)
    sum_num += num
print(sum_num)

for x in range(2,34,5):
    print(x)
for x in range(2,55,5):
    print(x)
    x_sum *= x
print(x_sum)     # outside the loop


