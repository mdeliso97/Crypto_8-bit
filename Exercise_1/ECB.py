from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

import codificator

'''
This class defines the logic of ECB symmetric encryption and decryption.
'''


# ECB encryption
def ecb_encrypt(file, password):
    BLOCK_SIZE = 32  # Bytes

    if password is None:
        # randomize key for encryption and decryption
        key = get_random_bytes(BLOCK_SIZE)
    else:
        password = codificator.decoding64(password)
        key = pad(password, BLOCK_SIZE)

    # create an AES cipher object in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)

    # perform padding and after encrypt plaintext
    encrypted_text = cipher.encrypt(pad(file, BLOCK_SIZE))

    if password is None:
        return encrypted_text, key
    else:
        return encrypted_text


# ECB decryption
def ecb_decrypt(message, key):
    BLOCK_SIZE = 32  # Bytes

    if not isinstance(key, (bytes, bytearray)):
        key = codificator.decoding64(key)
        key = pad(key, BLOCK_SIZE)

    # define ECB decipher with key
    decipher = AES.new(key, AES.MODE_ECB)

    # decrypt ciphertext
    decrypted_text = decipher.decrypt(message)

    # unpad decrypted ciphertext
    decrypted_text = unpad(decrypted_text, BLOCK_SIZE)

    return decrypted_text
