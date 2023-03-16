import random as rand


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
pass_1 = ''
pass_1 = ''
for alpha in range(1, int(alphabet_times)+1):
    pass_1 += pass_alpha[rand.randint(0, len(pass_alpha)-1)]   # list[n] shows n-1th element in list bcz index starts from 0 as 1st and n as n-1th element
for num in range(1, int(num_times)+1):
    pass_1 += rand.choice(pass_num)                            # choice function chose an element from a list
for num in range(1, int(s_carr_times)+1):
    pass_1 += rand.choice(pass_s_carr)

# change pass_1 string to List for shuffle the list using rand.shuffle(List)
pass_1_list = []
for list_member in pass_1:
    pass_1_list += [list_member]
print(pass_1_list)
# pass_1_list_shuffled = rand.shuffle(pass_1_list)   this is not valid
rand.shuffle(pass_1_list)  # this valid no need to store
# again converting list to strring
print(pass_1_list)
password = ''
for shuffled_list_member in pass_1_list:
    password += shuffled_list_member
print(password)




