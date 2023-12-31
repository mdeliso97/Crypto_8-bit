import json

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
from Utilities.codificator import encoding64, decoding64

'''
This class defines the logic of ECB symmetric encryption and decryption.
'''


# ECB encryption
def ecb_encrypt(file, password, filename, extension):
    BLOCK_SIZE = 32  # Bytes

    if password is None:
        # randomize key for encryption and decryption
        key = get_random_bytes(BLOCK_SIZE)
    else:
        # takes user password instead of random generated byte string
        password = decoding64(password)
        # performs padding to the password to make sure the length is correct
        key = pad(password, BLOCK_SIZE)

    # create an AES cipher object in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)

    # perform padding and after encrypt plaintext
    encrypted_text = cipher.encrypt(pad(file, BLOCK_SIZE))

    # convert to string ciphertext
    ct_key = encoding64(encrypted_text)

    json_output = json.dumps({'ciphertext': ct_key, 'filename': filename, 'extension': extension})

    if password is None:
        return json_output, key
    else:
        return json_output


# ECB decryption
def ecb_decrypt(json_file, key):
    BLOCK_SIZE = 32  # Bytes

    if not isinstance(key, (bytes, bytearray)):
        key = decoding64(key)
        key = pad(key, BLOCK_SIZE)

    json_file = json.loads(json_file)

    # retrieve initialization vector and ciphertext from json file
    ct_key = decoding64(json_file['ciphertext'])
    extension = json_file['extension']
    filename = json_file['filename']

    # define ECB decipher with key
    decipher = AES.new(key, AES.MODE_ECB)

    # decrypt ciphertext
    decrypted_text = decipher.decrypt(ct_key)

    # unpad decrypted ciphertext
    decrypted_text = unpad(decrypted_text, BLOCK_SIZE)

    return decrypted_text, filename, extension
