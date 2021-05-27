from Crypto.Cipher import AES
import hashlib

def manage_Image(filename):
    with open(filename, "rb") as image:
        f = image.read()
        allBytes = bytearray(f)
    header_size = 54
    headerBytes = allBytes[0:header_size]
    usabilityBytes = allBytes[header_size:]
    return headerBytes, usabilityBytes

def pad_message(file):
    while len(file)%16 != 0:
        file = file + b"0"
    return file

def encrypt_ECB(password,orig_file):
    try:
        key = hashlib.sha256(password.encode()).digest()
        mode = AES.MODE_ECB
        cipher = AES.new(key,mode)
        header, bytestoEncrypt = manage_Image(orig_file)
        padded_bytes = pad_message(bytestoEncrypt)
        encryptBytes = cipher.encrypt(padded_bytes)
        encrypted_file = header + encryptBytes
        with open('assets/'+orig_file[0:7]+'_eECB.bmp','wb') as e:
            e.write(encrypted_file)
        return "Cipher made successfully, the result is below this message and in the directory assets with the name '"+orig_file[0:7]+"_eECB.bmp'"
    except:
        return "Something went wrong"

def decrypt_ECB(password,orig_file):
    try:
        key = hashlib.sha256(password.encode()).digest()
        mode = AES.MODE_ECB
        cipher = AES.new(key, mode)
        header, bytestoDecrypt = manage_Image(orig_file)
        decryptBytes = cipher.decrypt(bytestoDecrypt)
        decrypted_file = header + decryptBytes
        with open('assets/'+orig_file[0:12]+'_dECB.bmp','wb') as e:
            e.write(decrypted_file)
        return "Decipher made successfully, the result is below this message and in the directory assets with the name '"+orig_file[0:12]+"_dECB.bmp'"
    except:
        return "Something went wrong"

def encrypt_CBC(password, IV, orig_file):
    try:
        key = hashlib.sha256(password.encode()).digest()
        mode = AES.MODE_CBC
        cipher = AES.new(key,mode,IV.encode())
        header, bytestoEncrypt = manage_Image(orig_file)
        padded_bytes = pad_message(bytestoEncrypt)
        encryptBytes = cipher.encrypt(padded_bytes)
        encrypted_file = header + encryptBytes
        with open('assets/'+orig_file[0:7]+'_eCBC.bmp','wb') as e:
            e.write(encrypted_file)
        return "Cipher made successfully, the result is below this message and in the directory assets with the name '"+orig_file[0:7]+"_eCBC.bmp'"
    except:
        return "Something went wrong"

def decrypt_CBC(password, IV, orig_file):
    try:
        key = hashlib.sha256(password.encode()).digest()
        mode = AES.MODE_CBC
        cipher = AES.new(key, mode, IV.encode())
        header, bytestoDecrypt = manage_Image(orig_file)
        decryptBytes = cipher.decrypt(bytestoDecrypt)
        decrypted_file = header + decryptBytes
        with open('assets/'+orig_file[0:12]+'_dCBC.bmp','wb') as e:
            e.write(decrypted_file)
        return "Decipher made successfully, the result is below this message and in the directory assets with the name '"+orig_file[0:12]+"_dCBC.bmp'"
    except:
        return "Something went wrong"

def encrypt_CFB(password, IV, orig_file):
    try:
        key = hashlib.sha256(password.encode()).digest()
        mode = AES.MODE_CFB
        cipher = AES.new(key,mode,IV.encode())
        header, bytestoEncrypt = manage_Image(orig_file)
        padded_bytes = pad_message(bytestoEncrypt)
        encryptBytes = cipher.encrypt(padded_bytes)
        encrypted_file = header + encryptBytes
        with open('assets/'+orig_file[0:7]+'_eCFB.bmp','wb') as e:
            e.write(encrypted_file)
        return "Cipher made successfully, the result is below this message and in the directory assets with the name '"+orig_file[0:7]+"_eCFB.bmp'"
    except:
        return "Something went wrong"

def decrypt_CFB(password, IV, orig_file):
    try:
        key = hashlib.sha256(password.encode()).digest()
        mode = AES.MODE_CFB
        cipher = AES.new(key, mode,IV.encode())
        header, bytestoDecrypt = manage_Image(orig_file)
        decryptBytes = cipher.decrypt(bytestoDecrypt)
        decrypted_file = header + decryptBytes
        with open('assets/'+orig_file[0:12]+'_dCFB.bmp','wb') as e:
            e.write(decrypted_file)
        return "Decipher made successfully, the result is below this message and in the directory assets with the name '"+orig_file[0:12]+"_dCFB.bmp'"
    except:
        return "Something went wrong"

def encrypt_OFB(password, IV, orig_file):
    try:
        key = hashlib.sha256(password.encode()).digest()
        mode = AES.MODE_OFB
        cipher = AES.new(key,mode,IV.encode())
        header, bytestoEncrypt = manage_Image(orig_file)
        padded_bytes = pad_message(bytestoEncrypt)
        encryptBytes = cipher.encrypt(padded_bytes)
        encrypted_file = header + encryptBytes
        with open('assets/'+orig_file[0:7]+'_eOFB.bmp','wb') as e:
            e.write(encrypted_file)
        return "Cipher made successfully, the result is below this message and in the directory assets with the name '"+orig_file[0:7]+"_eOFB.bmp'"
    except:
        return "Something went wrong"

def decrypt_OFB(password, IV, orig_file):
    try:
        key = hashlib.sha256(password.encode()).digest()
        mode = AES.MODE_OFB
        cipher = AES.new(key, mode,IV.encode())
        header, bytestoDecrypt = manage_Image(orig_file)
        decryptBytes = cipher.decrypt(bytestoDecrypt)
        decrypted_file = header + decryptBytes
        with open('assets/'+orig_file[0:12]+'_dOFB.bmp','wb') as e:
            e.write(decrypted_file)
        return "Decipher made successfully, the result is below this message and in the directory assets with the name '"+orig_file[0:12]+"_dOFB.bmp'"
    except:
        return "Something went wrong"