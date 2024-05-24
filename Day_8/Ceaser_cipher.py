logo="""
   _____                              _____ _       _               
  / ____|                            / ____(_)     | |              
 | |     __ _  ___  ___  __ _ _ __  | |     _ _ __ | |__   ___ _ __ 
 | |    / _` |/ _ \/ __|/ _` | '__| | |    | | '_ \| '_ \ / _ \ '__|
 | |___| (_| |  __/\__ \ (_| | |    | |____| | |_) | | | |  __/ |   
  \_____\__,_|\___||___/\__,_|_|     \_____|_| .__/|_| |_|\___|_|   
                                             | |                    
                                             |_|                    
"""

print(logo)

def encrypt(text, shift):
    cipher_text=""
    for i in range(len(text)):
        cipher_text+=chr(ord(text[i])+int(shift))
    
    return cipher_text

def decrypt(text, shift):
    cipher_text=""
    for i in range(len(text)):
        cipher_text+=chr(ord(text[i])-int(shift))
    
    return cipher_text

while(True):
    choice=input("Type 'encode' to encrypt and 'decode' to decrypt or any other key to exit: ")

    if choice == "encode":
        text = input("Type your message: ")
        shift = int(input("Type the shift number: "))
        cipher_text = encrypt(text, shift)
        print(f"The encoded text is {cipher_text}")
    elif choice=="decode":
        text = input("Type your message: ")
        shift = int(input("Type the shift number: "))
        cipher_text = decrypt(text, shift)
        print(f"The decoded text is {cipher_text}")
    else:
        break