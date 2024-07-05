#defining global variables commonly used in all functions
alpha = [x for x in 'abcdefghijklmnopqrstuvwxyz']
sub = []

def shift_check(x):
    #checks if the shift value is valid/invalid
    if 0<=x<=25: #range of 0-25 is used as there are only 26 alphabets
        return "Valid"
    else:
        return "Invalid shift value! Only accepted values are in range from 0-25."

def substitution(k):
    #updating the global var 'sub' to allow dynamic encryption/decryption
    if shift_check(k)=="Valid":
        for _ in range(0,len(alpha)):
            sub.append(alpha[(_+k) % len(alpha)])
        return sub
    else: #showing user what went wrong
        return shift_check(k)

def encrypt(msg):
    #encryption algorithm logic
    enc_msg = ""
    for i in msg:
        if i in '!@#$%^&*(){}[]|\\\'\":;<>?.,/~`_-+= 1234567890': #leaving the special chars and numbers unencrypted
            enc_msg+=i
        
        if i in alpha: 
            ele = alpha.index(i) #mapping each plain text letter in the plain text to its encrypted letter
            enc_msg = enc_msg + sub[ele] #appending the mapped cipher letter to the encrypted message
    return enc_msg

def decrypt(cipher):
    #decrpytion algorithm logic
    dec_msg = ""
    for i in cipher:
        if i in '!@#$%^&*(){}[]|\\\'\":;<>?.,/~`_-+= 1234567890': #leaving the special chars and numbers unencrypted
            dec_msg+=i
        if i in sub:
            ele = sub.index(i) #mapping each encrypted letter to its plain text letter
            dec_msg = dec_msg + alpha[ele] #appending the mapped plain text letter to the decrypted message
    return dec_msg

def caesar_cipher(msg, shift, func):
    #integrating all of the above individual functions 
    try:
        #double checking the user input values for data type conversions
        int(shift)
        str(msg)
        str(func)

    except Exception:
        print("Data type error") #internal error handling

    finally:
        substitution(shift) 
        
        if shift_check(shift)!="Valid": #showing user what went wrong
            print(shift_check(shift))

        if func.lower()=="encrypt":
            #implementing encryption
            print("Encrypted message is: " + encrypt(msg))

        elif func.lower()=="decrypt":
            #implementing decryption
            print("Decrypted message is: " + decrypt(msg))
            
        else: #validating and handling other possible user inputs 
            print("Invalid arguement passed! Only 'encrypt' and 'decrypt' keywords are allowed.")

#basic introduction and instructions on how to use the tool
print("\nWelcome to the Caesar Cipher Algorithm!\n")

#code menu for accesing different segments of the tool
print("\nCodes:")
print("- What Caesar cipher is > define")
print("- Work it out by yourself > go")
print("- Exit > bye\n\n")

#interactive 
while(True):
    choice = str(input("Enter code here to access a section: ")).strip()

    if choice.lower()=="go": #for performing encryption/decryption
        print("Let's see how easy it is to implement this algorithm.... ")
        print("\n- Ensure that your message does not contain any special characters or number.\n")
        msg = str(input("\nEnter your secret message here -> ")).strip()
        shift = int(input("\nEnter the shift value -> "))
        op = str(input("\nEnter operation type (encrypt/decrypt) -> ")).strip()

        caesar_cipher(msg,shift,op)

    elif choice.lower()=="define": #for learning what is caesar cipher and how it works 
        print("\nDefinition:A Caesar cipher is a substitution cipher in which each letter in the plaintext is shifted a fixed number of places down the alphabet.\nFor example, with a shift of 3, A would be replaced by D, B would become E, and so on.\n\n This method is used to encode messages by transforming them into an unreadable format unless the recipient knows the shift value to decode it.")
        print("\nIt is named after Julius Caesar, who used this method to protect his military communications.\n One of the earliest recorded uses of encryption, Caesar shifted his messages by three places to keep them secret from his enemies.")

    elif choice.lower()=="bye": #exitting 
        break

    else: #handling any other user inputs
        print("Invalid code! Please try again with a valid code.")
    print("\nCodes -> define, go, bye\n") #incase user forgets te codes 