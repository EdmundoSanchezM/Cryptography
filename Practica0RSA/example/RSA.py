from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import os
script_dir = os.path.dirname(__file__) 

def cypher(file,PK):
    f=open(file,"rb")
    mensaje=f.read()
    llave=PK
    key=RSA.importKey(open(llave,"rb").read())
    cifrado=PKCS1_OAEP.new(key)
    ciframessage = cifrado.encrypt(mensaje)
    f = open("message_C.txt","wb")
    f.write(ciframessage)
    f.close()
    return "Cypher made successfully, plese check your directory"

def decipher(file,PVK):
    try:
        f=open(file,"rb")
        mensaje = f.read()
        llave=PVK
        key=RSA.importKey(open(llave,"rb").read())
        cifrado=PKCS1_OAEP.new(key)
        f.close()
        ciframessage = cifrado.decrypt(mensaje)
        f = open("message_C_D.txt","wb")
        f.write(ciframessage)
        f.close()
        return "Decipher made successfully, plese check your directory"
    except:
        return "Error Decryption"