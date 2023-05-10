import pyAesCrypt
import os

# encrypt
enc_password = os.path.join('password')
pyAesCrypt.encryptFile('password.txt', 'password.txt.aes', enc_password)

#decrypt
dec_password = os.path.join('password')
pyAesCrypt.decryptFile('password.txt.aes', 'password_out.txt', dec_password)

