def dialog_message():
    return ("Welcome to Crypto 8-bit \n\n"
            "This program is used to encrypt or decrypt files for security reasons."
            "To use the program correctly, follow a top-down approach, following "
            "the different checkboxes and buttons from the top until down to the bottom.\n\n"
            "The symmetric cipher approach to encrypt/decrypt allows to put your own "
            "password instead of the program generating one for you. When if you do not"
            "wish to use your own password, just skip the password input box. Don't forget "
            "your password if you wish to use one the program will not store it locally, "
            "so you will lose it forever if you forget it. After you choose which cipher "
            "mode to use you can proceed choosing encryption or decryption.\n\n"
            "Encryption is quite easy, in symmetric encryption, you will be asked for the"
            "file you want to encrypt and as soon as you press the start button, you will"
            "get two files as output, which will show in the same directory or your "
            "program, one is the automatic generated key (if you did not use the password) "
            "the second one is the encrypted file you gave as input, follow the information "
            "prompted into the console for more details.\n\n"
            "Decryption to work needs two parameters when using symmetric method, use "
            "source file button to upload your encrypted file and the source key button "
            "to source for the key you used beforehand to encrypt (or directly insert the "
            "password). The output file is the decrypted file. \n\n"
            "The Asymmetric method works only by selecting both a symmetric AEAD cipher "
            "(in this program, GCM is the only AEAD symmetric cipher provided) and an "
            "asymmetric cipher, check the checkbox sym/asym to switch between the two and "
            "select according your preferences. Make sure to leave the asymmetric option "
            "otherwise you will get an error message (because it is trying to encrypt with "
            "symmetric method). The asymmetric method needs two extra keys to work, namely "
            "the public key and the private key, to generate a pair, press keygen button. "
            "After this step, the encryption works quite similar to the symmetric method, "
            "except for uploading the the file and the public key as well. "
            "As output you will get an encrypted key, which was used to encrypt the file "
            "and the encrypted file itself.\n"
            "Decryption needs in total three parameters to work, the encrypted file, the"
            "encrypted key and the private key. As soon as you uploaded all of these and "
            "press start button, you will get as output the decrypted file.\n\n"
            "During all these manipulations, the console located to the bottom will guide "
            "you towards a correct workflow. Thanks for reading and enjoy cryptography!")
