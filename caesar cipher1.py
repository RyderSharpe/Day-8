alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    
    alphabet_length = 26
    cipher_text = ""

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            base = ord('a') if char.islower() else ord('A')  # Set the base depending on lowercase or uppercase
            shifted_char = chr((ord(char) - base + shift) % alphabet_length + base)
            cipher_text += shifted_char
        else:
            cipher_text += char

    print(f"The encoded text is {cipher_text}")

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(text, shift)
