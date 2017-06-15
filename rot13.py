import string
def crypt13(string):
    """This decrypts and encrypts string using ROT 13.5"""
    new_char=''
    out=''
    for i in string:
        if i.isalpha() == True:
            if i.isupper() == True:
                if (ord(i)+13) > 90:
                    new_char = chr((ord(i)-13))
                else:
                    new_char = chr((ord(i) + 13))
            elif i.islower() == True:
                if (ord(i)+13) > 122:
                    new_char = chr((ord(i)-13))
                else:
                    new_char = chr((ord(i) + 13))
        elif i.isdigit() == True:
            if int(i)+5 > 9:
                new_char=str(int(i)-5)
            else:
                new_char=str(int(i)+5)
        else:
            new_char=i
        out=out+str(new_char)
    print(out)

#main
user_input = input("input the string to be encrypted/decrypted \n")
crypt13(user_input)