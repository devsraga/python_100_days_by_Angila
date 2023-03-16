def encrypt(code, shift, alphabet_list):
    encrypt = ''
    for letter in code:
        ind = 0
        if letter in alphabet_list:
            checking = True
            while checking:
                if letter == alphabet_list[ind]:
                    checking = False
                else:
                    ind += 1
            shifted = shift + ind
            if shifted > 25:
                shifted = shifted - 26
            elif shifted < 0:
                shifted = 26 + shifted
            encrypt += alphabet_list[shifted]
        else:
            encrypt += letter
    print(f"your encrypt is:  {encrypt}")


def decrypt(code, shift, alphabet_list):
    decrypt = ''
    for letter in code:
        ind = 0
        if letter in alphabet_list:
            checking = True
            while checking:
                if letter == alphabet_list[ind]:
                    checking = False
                else:
                    ind += 1
            shifted = ind - shift
            if shifted > 25:
                shifted = shifted - 26
            elif shifted < 0:
                shifted = 26 + shifted
            decrypt += alphabet_list[shifted]
        else:
            decrypt += letter
    print(f"your encrypt is:  {decrypt}")


def ceser_ciper():
    will = True
    while will:
        alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
        alphabet_list = alphabet.split(",")
        query = input("you want encrypt are decode press e or d: ")
        code = input("Enter code: ").lower()
        shift = int(input("Enter Shifts: "))
        if query == 'e':
            encrypt(code, shift, alphabet_list)
        elif query == 'd':
            decrypt(code, shift,alphabet_list)
        will_of_user = input("Do you want to go further. For yes- 'y' and No- 'N':  ").lower()
        if will_of_user == 'n':
            will = False
        elif will_of_user == 'y':
            will = True
        else:
            will = False
            print("Sorry, because of wrong entry ciser ciper is stoping... ")


ceser_ciper()

# index_in_list = list.index(element)  will give index
