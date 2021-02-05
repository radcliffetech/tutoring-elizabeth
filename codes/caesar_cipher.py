# CAESAR CIPHER

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # abcdefghijklmnopqrstuvwxyz1234567890 !?.'


def do_caesar_cipher(message, key, mode):

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


if __name__ == "__main__":

    # encrypt a message
    encrypted_message = do_caesar_cipher(
        'Cheese and crackers are very tasty!',
        key=13,
        mode='encrypt'
    )
    print("Encrypted:", encrypted_message)

    # decrypt
    decrypted_message = do_caesar_cipher(
        encrypted_message,
        key=13,
        mode='decrypt'
        )
    print("Decrypted:", decrypted_message)
