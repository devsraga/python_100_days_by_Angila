
list_of_stu_score = input("Enter the score of students separated by coma: ").split(",")
b = 0
score_list = []
score_list_append = []
for score in list_of_stu_score:
    score_list += [score]
    score_list_append.append(score)   # appending the list from null [] to string elements
    a = int(score)

    if a > b:
        b = a
    else:
        b = b
print(f"The highest score is: {b}")
print(score_list)
print(score_list_append)
for num in range(1, 100):
    print(num)
print("Dev")
print(num)

total = 0
for val in range(1, 101):
    total += val
print(total)
evn_total = 0
for even_num in range(2,101,2):
    evn_total += even_num
print(evn_total)
        





