import string

def shift_digit(digit):
    if int(digit) + 5 > 9:
         return(str(int(digit) - 5))
    else:
        return(str(int(digit) + 5))

def shift_letter(letter):
    if letter.isupper() == True:
        if (ord(letter) + 13) > 90:
            return(chr((ord(letter) - 13)))
        else:
            return(chr((ord(letter) + 13)))
    elif letter.islower() == True:
        if (ord(letter) + 13) > 122:
            return(chr((ord(letter) - 13)))
        else:
            return(chr((ord(letter) + 13)))

def crypt13(string):
    """This decrypts and encrypts string using ROT 13.5"""
    out=''
    for i in string:
        if i.isalpha() == True:
            out+=shift_letter(i)
        elif i.isdigit() == True:
            out+=shift_digit(i)
        else:
            out+=str(i)

    print(out)

def menu():
    active = True
    while active == True:
        user_input = input("\ninput the string to be encrypted/decrypted \n")
        crypt13(user_input)
        cont = input("\nwould you like to do another? (yes/no) \n")
        if cont == "no":
            print("\nGoodbye!")
            active = False
        elif cont != "yes":
            print("Please select yes or no \n")

#main
menu()
