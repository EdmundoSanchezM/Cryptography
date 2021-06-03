from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES, PKCS1_OAEP
import random
import string
from typing import KeysView
from Crypto import PublicKey
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii
from Crypto.Random import get_random_bytes
# Padding for the input string --not
# related to encryption itself.
BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

direccion="C:/Users/memo0/Desktop/pcriptp/"
class AESCipher:

    def __init__(self, key):
        self.key = md5(key.encode('utf8')).hexdigest()

    def encrypt(self, raw):
        raw = pad(raw)
        cipher = AES.new(self.key.encode("utf8"), AES.MODE_ECB)
        return b64encode(cipher.encrypt(raw.encode('utf8')))

    def decrypt(self, enc):
        enc = b64decode(enc)
        cipher = AES.new(self.key.encode("utf8"), AES.MODE_ECB)
        return unpad(cipher.decrypt(enc)).decode('utf8')
def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))
def openFile(filename):
    f=open(filename,"r")
    mensaje=f.read()
    f.close
    return mensaje
def cifrarTexto():
    mensaje = openFile(direccion+'mensaje.txt')
    pwd=random_char(16)
    c=AESCipher(pwd).encrypt(mensaje)
    out = open (direccion+'cifrado.txt','wb')
    out.write(c)
    out.write(b'\n--------------------------------------\n')
    out.close()
    return pwd
    
def descifrarTexto(pwd):
    mensaje = openFile(direccion+'cifrado.txt')
    p=AESCipher(pwd).decrypt(mensaje)
    out = open (direccion+'descifrado.txt','w')
    out.write(p)
    out.write('\n--------------------------------------\n')
    out.close()

def cifrarcontra(pwd):
    data=pwd.encode("utf-8")
    out = open (direccion+'cifrado.txt','ab')
    recipient_key = RSA.import_key(open(direccion+"PublicKeyCandy.pem").read())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    [ out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    out.write(b'\n--------------------------------------\n')
    out.close()
    
def sacarLlave():
    archivo = open(direccion+"cifrado.txt", "rb") 
    msg_sign=str(archivo.read())
    msgaux=msg_sign.split('\\n--------------------------------------\\n')
    print("llave:",msgaux[1])
    aux=msgaux[1].encode()
    archivo.close()
    out = open (direccion+'cifradocontra.txt','wb')
    out.write(aux)
    out.close()
    
def descifrarcontra():  
    sacarLlave()
    file_in = open(direccion+"cifradocontra.txt", "rb")  
    private_key = RSA.import_key(open(direccion+"PrivateKeyCandy.pem").read())
    enc_session_key, nonce, tag, ciphertext = \
    [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

    # Decrypt the session key with the private RSA key
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    # Decrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    out = open (direccion+'descifrado.txt','wb')
    out.write(data)
    out.write('\n--------------------------------------\n')
    out.close()
    return data
    
contra=cifrarTexto()
cifrarcontra(contra)
contra=descifrarcontra()
descifrarTexto(contra)
print("contraseña: ",contra)

# print("1 para cifrar y firma")
# print("2 para descifrado y verificacion")
# var=int(input())
# if(var==1):
#     print("hola")
#     contra=cifrarTexto()
#     cifrarcontra(contra)
# elif(var==2):
#     contra=descifrarcontra()
#     descifrarTexto(contra)
#     print("contraseña: ",contra)


