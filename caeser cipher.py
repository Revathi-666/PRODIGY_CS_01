def encrypt(text, shift):
    result = ""
    
    # traverse text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's not a letter, just add it as it is
        else:
            result += char
    
    return result

# Example usage
text = "caeser , cipher !"
# A = g  ,  B = h
shift = 6
encrypted_text = encrypt(text, shift)
print("Encrypted Text: " + encrypted_text)

def decrypt(text, shift):
    return encrypt(text, -shift)

# Example usage
decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted Text: " + decrypted_text)
