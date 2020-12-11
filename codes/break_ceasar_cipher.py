from caesar_cipher import do_caesar_cipher, SYMBOLS
from detect_english import detect_english


number_keys = len(SYMBOLS)

# this is my secret message to you
# message = "zKPINGmDGNNUpmLKPINGmDGNNUpzKPINGmCNNmVJGmYCap5JpmYJCVmHWPmKVmKUmVQmTKFGpyPmCmQPGmJQTUGmQRGPmUNGKIJ"

message = "278  8?6VH8E7VE74V1C.D"

# CODE BREAKING VIA BRUTE FORCE

for key in range(number_keys):

    decrypted_message = do_caesar_cipher(
        message,
        key=key,
        mode='decrypt'
        )
    if detect_english(decrypted_message):
        print(key, '\t', decrypted_message)
        print("")
