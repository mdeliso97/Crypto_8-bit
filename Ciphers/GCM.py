import json

from Utilities.codificator import encoding64, decoding64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

'''
This class defines the logic of AEAD AES-GCM symmetric encryption and decryption. 
'''


# GCM encryption
def gcm_encrypt(file, password, filename, extension):
    BLOCK_SIZE = 32

    if password is None:
        # randomize key for encryption and decryption
        key = get_random_bytes(BLOCK_SIZE)
    else:
        # takes user password instead of random generated byte string
        password = decoding64(password)
        # performs padding to the password to make sure the length is correct
        key = pad(password, BLOCK_SIZE)

    # Generate a random 96-bit key
    nonce_key = get_random_bytes(12)  # 96 bits = 12 bytes (AES-GCM requires a 12-byte nonce)

    # initialize the AES-GCM cipher with the key
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce_key)

    # Encrypt the plaintext
    key_ct, key_tag = cipher.encrypt_and_digest(file)

    tag_key = encoding64(key_tag)
    ct_key = encoding64(key_ct)
    nonce_key = encoding64(nonce_key)

    # store nonce, tag and ciphertext into a json file
    json_output = json.dumps(
        {'nonce': nonce_key, 'tag': tag_key, 'ciphertext': ct_key, 'filename': filename, 'extension': extension})

    if password is None:
        return json_output, key
    else:
        return json_output


# GCM decryption
def gcm_decrypt(json_file, key):
    BLOCK_SIZE = 32

    if not isinstance(key, (bytes, bytearray)):
        key = decoding64(key)
        key = pad(key, BLOCK_SIZE)

    json_file = json.loads(json_file)

    # retrieve nonce, tag and encrypted file
    key_nonce = decoding64(json_file['nonce'])
    key_tag = decoding64(json_file['tag'])
    key_ct = decoding64(json_file['ciphertext'])
    filename = json_file['filename']
    extension = json_file['extension']

    # define decipher and couple it with nonce byte string
    decipher = AES.new(key, AES.MODE_GCM, nonce=key_nonce)

    # decrypt ciphertext
    file_decrypted = decipher.decrypt_and_verify(key_ct, key_tag)

    return file_decrypted, filename, extension
