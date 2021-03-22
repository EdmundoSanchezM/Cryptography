import random
import os
script_dir = os.path.dirname(__file__) 

alphabet = "abcdefghijklmnopqrstuvwxyz "
auxkey = "abcdefghijklmnopqrstuvwxyz"

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def generatekey(sizemsg):
    tamañokey = random.randrange(sizemsg)
    key = ""
    for i in range(tamañokey):
        while True:
            letra = random.choice(auxkey)
            if letra!=' ':
                key += letra
                i=i
                break
    return key

def encrypt(file,keyS):
    try:
        f=open(file,"r")
        message=f.read()
        f.close()
        key = str(keyS)
        returnMessage = "Cypher made successfully plese check your directory"
        
        if(keyS == "777"):
            key = generatekey(len(message))
            returnMessage +=" the key generate is ' "+ key +" '"
        encrypted = ""
        split_message = [
            message[i : i + len(key)] for i in range(0, len(message), len(key))
        ]

        for each_split in split_message:
            i = 0
            for letter in each_split:
                number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
                encrypted += index_to_letter[number]
                i += 1

        f = open("encrypt.vig","w")
        f.write(encrypted)
        f.close
        return returnMessage
    except:
        return  "Error encrypt"


def decrypt(file,keyS):
    try:
        f=open(file,"r")
        cipher=f.read()
        f.close()
        key=str(keyS)
        decrypted = ""
        split_encrypted = [
            cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))
        ]

        for each_split in split_encrypted:
            i = 0
            for letter in each_split:
                number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
                decrypted += index_to_letter[number]
                i += 1

        f = open("decrypt.vig","w")
        f.write(decrypted)
        f.close
        return "Decipher made successfully, plese check your directory"
    except:
        return "Error Decryption"
