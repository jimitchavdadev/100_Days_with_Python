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
    """Encrypts a given text using a Caesar cipher with the specified shift."""
    cipher_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            cipher_text += shifted_char if char.islower() else shifted_char.upper()  # Preserve case
        else:
            cipher_text += char  # Keep non-alphabetic characters unchanged
    return cipher_text

def decrypt(text, shift):
    """Decrypts a given text using a Caesar cipher with the specified shift."""
    return encrypt(text, -shift)  # Decrypting is essentially encrypting with negative shift

while True:
    choice = input("Type 'encode' to encrypt and 'decode' to decrypt or any other key to exit: ")

    if choice.lower() == "encode" or choice.lower() == "decode":
        text = input("Type your message: ")
        shift = int(input("Type the shift number: "))
        if choice.lower() == "encode":
            result = encrypt(text, shift)
            print(f"The encoded text is: {result}")
        else:
            result = decrypt(text, shift)
            print(f"The decoded text is: {result}")
    else:
        break