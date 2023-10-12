from GCM import *


def rsa_oaep_encryption(file, json_pub):
    # Retrieve GCM AEAD cipher's outputs
    json_output, key = gcm_encryption(file)

    json_pub = json.loads(json_pub)

    n_key = json_pub['n']
    pub_key = json_pub['public']

    key = int.from_bytes(key, byteorder='little')

    # ToDo: M < n, C = M^e (mod n)

    if len(str(key)) < len(str(n_key)):
        key_encrypt = pow(key, pub_key, n_key)
    else:
        return print("error occurred: length not respected -> M < n")

    return json_output, key_encrypt


def rsa_oaep_decryption(json_file, key_encrypt, json_key_private):
    json_key = json.loads(json_key_private)

    private_key = json_key["private"]
    n_key = json_key['n']

    key_encrypt = int(key_encrypt)

    # C = ciphertext, M = C^d (mod n)
    pub_decrypt_key = pow(key_encrypt, private_key, n_key)

    pub_decrypt_key = pub_decrypt_key.to_bytes(32, byteorder='little')

    key_decrypted = gcm_decryption(json_file, pub_decrypt_key)

    # key_decipher = AES.new(key_private, AES.MODE_GCM, nonce=nonce_key)
    # key_decrypted = key_decipher.decrypt_and_verify(key_encrypt, tag_key)
    # file_decipher = AES.new(key_decrypted, AES.MODE_GCM, nonce=nonce_key)
    # file_decrypted = file_decipher.decrypt_and_verify(ct_key, tag_key)

    return key_decrypted
