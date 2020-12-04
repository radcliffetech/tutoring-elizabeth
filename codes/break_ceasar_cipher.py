from caesar_cipher import do_caesar_cipher, SYMBOLS

number_keys = len(SYMBOLS)

# this is my secret message to you
message = "zKPINGmDGNNUpmLKPINGmDGNNUpzKPINGmCNNmVJGmYCap5JpmYJCVmHWPmKVmKUmVQmTKFGpyPmCmQPGmJQTUGmQRGPmUNGKIJ"

# CODE BREAKING VIA BRUTE FORCE

for key in range(number_keys):

    decrypted_message = do_caesar_cipher(
        message,
        key=key,
        mode='decrypt'
        )
    print(key, '\t', decrypted_message)
    print("")
