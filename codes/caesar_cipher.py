# CAESAR CIPHER

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

key = 13


def caesar_cipher(message, mode):

    translated_message = ''

    for letter in message:
        index = SYMBOLS.find(letter)
        # move forward/backword by "KEY"
        if mode == 'encrypt':
            translated_index = index + key
        else:
            translated_index = index - key

        # adjust for wraparound
        if translated_index >= len(SYMBOLS):
            # wrap around from the end
            translated_index = translated_index - len(SYMBOLS)
        elif translated_index < 0:
            # wrap around from the start!
            translated_index = translated_index + len(SYMBOLS)

        translated_message = translated_message + SYMBOLS[translated_index]

    return translated_message


# encrypt a message
encrypted_message = caesar_cipher('Cheese and crackers are very tasty!', mode='encrypt')
print("Encrypted:", encrypted_message)

# decrypt
decrypted_message = caesar_cipher(encrypted_message, mode='decrypt')
print("Decrypted:", decrypted_message)
