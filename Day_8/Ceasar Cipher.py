# Ceasar Cipher 

logo="""
                                                                  
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88          

           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                    
"""

def encrypt(message,shift):
    encrypted=[]
    for i in range(len(message)):
        encrypted.append(chr(ord(message[i])+shift))
    return encrypted

def decrypt(message,shift):
    decrypted=[]
    for i in range(len(message)):
        decrypted.append(chr(ord(message[i])-shift))
    return decrypted

def print_list(list):
    for i in list:
        print(i,end="")

print(logo)
print("Welcome to Ceasar Cipher")

print(logo)
print("Welcome to Caesar Cipher")

choice = ""
while choice != "q":
    choice = input("Do you want to encrypt, decrypt, or quit (e/d/q): ")

    if choice == "e":
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift number: "))
        cipher_text = encrypt(message, shift)
        print(f"Your encrypted message is:")
        print_list(cipher_text)
        print()

    elif choice == "d":
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift number: "))
        plain_text = decrypt(message, shift)
        print(f"Your decrypted message is:")
        print_list(plain_text)
        print()

    elif choice == "q":
        print("Quitting the Caesar Cipher program.")
    else:
        print("Invalid choice. Please enter 'e', 'd', or 'q'.")
