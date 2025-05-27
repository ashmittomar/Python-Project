def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

print("Caesar Cipher Program")
choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

if choice == 'e':
    plain_text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value (e.g., 3): "))
    encrypted_text = encrypt(plain_text, shift)
    print("Encrypted text:", encrypted_text)

elif choice == 'd':
    cipher_text = input("Enter the text to decrypt: ")
    shift = int(input("Enter the shift value used for encryption: "))
    decrypted_text = decrypt(cipher_text, shift)
    print("Decrypted text:", decrypted_text)

else:
    print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")
