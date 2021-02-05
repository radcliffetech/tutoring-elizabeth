from caesar_cipher import do_caesar_cipher, SYMBOLS
from detect_english import detect_english


number_keys = len(SYMBOLS)

# this is my secret message to you
# message = "zKPINGmDGNNUpmLKPINGmDGNNUpzKPINGmCNNmVJGmYCap5JpmYJCVmHWPmKVmKUmVQmTKFGpyPmCmQPGmJQTUGmQRGPmUNGKIJ"

message = """NSRRFSY"""

# CODE BREAKING VIA BRUTE FORCE

# for key in range(number_keys):

decrypted_message = do_caesar_cipher(
    message,
    key=4,
    mode='decrypt'
    )
# if detect_english(decrypted_message):
#     print(key, '\t', decrypted_message)
#     print("")

print(decrypted_message)
