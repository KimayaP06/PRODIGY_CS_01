def caesar_cipher(message, mode, shift):
    result = ""
    for char in message:
        if char.isalpha():  # Only process alphabetic characters
            start = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo

            shifted_char = chr((ord(char) - start + (shift if mode == "encrypt" else -shift)) % 26 + start)
            result += shifted_char
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

# Get inputs from the user
message = input("Enter your message: ")
mode = input("Choose mode (encrypt / decrypt): ").strip().lower()
shift = int(input("Enter the shift value (0-25): "))

# Validate mode
if mode not in ["encrypt", "decrypt"]:
    print("Invalid mode. Please choose 'encrypt or 'decrypt.")
else:
    # Perform the Caesar Cipher
    result = caesar_cipher(message, mode, shift)
    print(f"The {mode}ed message is: {result}")
