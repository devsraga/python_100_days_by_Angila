
row_1 = ["☺","☺","☺"]
row_2 = ["☺","☺","☺"]
row_3 = ["☺","☺","☺"]
map = [row_1, row_2, row_3]

mat_index = input("Enter matrix element index other than 11:  ")
horizontal = int(mat_index[0]) - 1
verticle = int(mat_index[1]) - 1
map[horizontal][verticle] = "D"
map[0][0] = "P"
print(f"{row_1}\n{row_2}\n{row_3}")
