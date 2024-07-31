from art import logo

# print the logo from the art.py file
print(logo)


# encrypting code function

def encrypt(text, shift):
    cipher_text = ""    
    # initialising an empty string
    
    for char in text:
        if char.islower():  # for lower case  
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            cipher_text += shifted_char
        elif char.isupper():    # for upper case
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            cipher_text += shifted_char
        elif char.isdigit():    # for digits
            shifted_char = chr((ord(char) - ord('0') + shift) % 10 + ord('0'))
            cipher_text += shifted_char
        else:
            cipher_text += char  # non-alphabetic characters remain unchanged
    return cipher_text


# decrypting code function

def decrypt(text, shift):
    return encrypt(text, -shift)  # Decrypting is just encrypting with negative shift


# main block of code

while True:
    # The loop will keep running till no other output other than e or d is given 
    choice = input("Type 'e' to encrypt and 'd' to decrypt or any other key to exit: ")

    if choice.lower() == "e" or choice.lower() == "d":
        text = input("Type your message: ")
        shift = int(input("Type the shift number: "))
        
        if choice.lower() == "e":
            result = encrypt(text, shift)
            print(f"The encoded text is: {result}")
        else:
            result = decrypt(text, shift)
            print(f"The decoded text is: {result}")
    else:
        break
