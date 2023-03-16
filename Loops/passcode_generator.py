import random

print("Welcome to password generator")
alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
num = "1,2,3,4,5,6,7,8,9,0"
s_carr = "!,@,#,$,%,^,&,*,(,),_"
pass_alpha = alphabet.split(",")
pass_num = num.split(",")
pass_s_carr = s_carr.split(",")
alphabet_times = input(f"How many alphabet want in your passcode, but enter less than or equal to {len(pass_alpha)}: ")
num_times = input(f"How many numbers want in passcode, but enter less than or equal to {len(pass_num)}: ")
s_carr_times = input(f"How many special characters want in passcode, but enter less than or equal to {len(pass_s_carr)} : ")
pass_1_total = ''  # declaring null string
pass_2_total = ''
pass_3_total = ''
pass_4_total = ''

for pass_1 in range(1,int(alphabet_times)+1):    # range(from,to) difference by default is 1
    pass_1_rand = random.randint(0, len(pass_alpha)-1)
    pass_1_total = pass_1_total + pass_alpha[pass_1_rand]

for pass_2 in range(1,int(num_times)+1):
    pass_2_rand = random.randint(0, len(pass_num)-1)  # random.randint(from, to) gives integer value
    print(pass_2_rand)
    pass_2_total = pass_2_total + pass_num[pass_2_rand]

for pass_3 in range(1, int(s_carr_times) + 1):
    pass_3_rand = random.randint(0, len(pass_s_carr)-1)  # len() is used for calculating length of vector
    pass_3_total = pass_3_total + pass_s_carr[pass_3_rand]
#     print(pass_3_rand)
# print(pass_3_total)
#print(f"Your generated passcode is: {pass_1_total}{pass_2_total}{pass_3_total}")  # *** low lavel
full_pass_1 = pass_1_total+pass_2_total+pass_3_total

# print(len(full_pass_1))
# last_rand_list = None
# for pass_4 in range(0, len(full_pass_1)):
#     last_rand = random.randint(0, len(full_pass_1)-1)
#      while last_rand == last_rand_list[:]:
#          last_rand = random.randint(0, len(full_pass_1) - 1)
#
#     last_rand_list = last_rand_list, last_rand
#     pass_4_total = pass_4_total + full_pass_1[last_rand]
#
# print(pass_4_total)
full_pass_2 = []    # declaration of array
for password in full_pass_1:
    full_pass_2 += [password]
#print(full_pass_2)
random.shuffle(full_pass_2)
#print(full_pass_2)
full_pass_3 = ''
for password in full_pass_2:
    full_pass_3 += password
print(f"Your password is: {full_pass_3}")  # used f string for variable using {} bracket

