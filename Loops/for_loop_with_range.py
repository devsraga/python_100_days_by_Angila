sum_of_100_odd_num = 0
ind = 0
odd_num_till_100 = []
for num in range(1,101,2):  # it will not include last number
    #odd_num_till_100 = [odd_num_till_100, num] -------- it is not working here but in mat
    # matlab --- [[[[0,1],3],5],7,......] or (((((0,1),3),5,)7,)9) so on
    odd_num_till_100.append(num)
    # odd_num_till_100 = odd_num_till_100 + [num]   it will also work
    # odd_num_till_100 += [num]   it will also work
    sum_of_100_odd_num += num
    ind += 1
###########################################################
print(f"odd_num_till_100:\n{odd_num_till_100}")
print(f"sum of odd_num_till_100:\n{sum_of_100_odd_num}")
avg = sum_of_100_odd_num/ind
print(f"average of first {ind} odd numbers is:\n{avg} ")


############################################################
print("\nsome Examples")
print(sum(range(1,100,2)))
print(sum(range(1,100,2))/len(range(1,100,2)))