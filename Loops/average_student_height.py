# Calculation of average student height...
heights = input("Please enter heights seperated by spase: ").split()
sum_of_heights = 0
number_of_student = 0
for height in heights:
    sum_of_heights += int(height)
    print(int(height))
    number_of_student += 1
print(heights)

print(f"number of students are: {number_of_student}")
print(f"heights are: {sum_of_heights}")
average_height = sum_of_heights/number_of_student
print(f"avarage heights are: {round(average_height)}")




