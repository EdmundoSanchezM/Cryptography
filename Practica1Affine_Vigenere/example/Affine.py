from math import floor
import random
import os
script_dir = os.path.dirname(__file__) 

def extendidoEuclides(a, b):
    if b == 0:
        return 0,1,0
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1
    while b != 0:
        q = a//b
        r = a - b * q
        u = u0 - q * u1
        v = v0 - q * v1
        a = b
        b = r
        u0 = u1
        u1 = u
        v0 = v1
        v1 = v
    return  a, u0, v0

def generateRandom(longitud):
    m = []
    for i in range(1,longitud):
        m.append(i)
    maux = []
    for i in m:
        if(extendidoEuclides(i,longitud)[0]==1):
            maux.append(i)
    return random.choice(maux),random.randint(0,longitud)

def inversoMultiplicativo(n, a):
    mcd , u , v = extendidoEuclides(a,n)
    if mcd != 1:
        print("No existe inverso")
        return 0
    if u>0:
        return u
    else:
        return n+u

def Encrypt(archivo, alphabet, alpha, beta):
    f=open(archivo,"r")
    texto=f.read()
    f.close()
    mensaje = "Cypher made successfully plese check your directory"
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    bandera = True
    esNumero = False
    try:
        numero = int(alphabet)
        esNumero = True
    except:
        esNumero = False
    if esNumero:
        alfabeto = [chr(i) for i in range(int(alphabet))]
        bandera = False
    elif ',' in alphabet:
        alfabeto = alphabet.replace(',', '')
    elif alphabet == "ES":
        alfabeto = "abcdefghijklmnñopqrstuvwxyz "
    elif alphabet == "D":
        alfabeto= "0123456789"
    elif alphabet == "ASCII":
        alfabeto = [chr(i) for i in range(256)]
        bandera = False
    if(alpha == 777 and beta == 777):
        alpha,beta = generateRandom(len(alfabeto))
        mensaje += ", alpha value = " + str(alpha) + " beta value = " + str(beta) 
    if(extendidoEuclides(alpha,len(alfabeto))[0]==1 and alpha<len(alfabeto)):
        textoCifrado = ""
        try: 
            if bandera:
                for p in texto:
                    textoCifrado += alfabeto[((alpha * alfabeto.find(p) )+ beta) % len(alfabeto)]
            else:
                for p in texto:
                    textoCifrado += alfabeto[((alpha * alfabeto.index(p) )+ beta) % len(alfabeto)]
            f = open("encrypt.aff","w",encoding="iso-8859-1")
            f.write(textoCifrado)
            f.close
            return mensaje
        except:
            return "Error encrypting"
    else:
        return "Alpha value not valid"

def InversoAditivo(beta,n):
    return int(n-beta%n)

def Decrypt(archivo, alphabet, alpha, beta):
    try:
        f=open(archivo,"r",encoding="iso-8859-1")
        textoCifrado=f.read()
        f.close()
        alfabeto = "abcdefghijklmnopqrstuvwxyz "
        bandera = True
        esNumero = False
        try:
            numero = int(alphabet)
            esNumero = True
        except:
            esNumero = False
        if esNumero:
            alfabeto = [chr(i) for i in range(int(alphabet))]
            bandera = False
        elif ',' in alphabet:
            alfabeto = alphabet.replace(',', '')
        elif alphabet == "ES":
            alfabeto = "abcdefghijklmnñopqrstuvwxyz "
        elif alphabet == "D":
            alfabeto= "0123456789"
        elif alphabet == "ASCII":
            alfabeto = [chr(i) for i in range(256)]
            bandera = False
        inversoalpha = inversoMultiplicativo(len(alfabeto),alpha)
        minusbeta = InversoAditivo(beta,len(alfabeto))
        textoDescifrado = ""
        if bandera:
            for c in textoCifrado:
                textoDescifrado += alfabeto[ (inversoalpha * (alfabeto.find(c) + minusbeta)) % len(alfabeto)]
        else:
            for c in textoCifrado:
                textoDescifrado += alfabeto[ (inversoalpha * (alfabeto.index(c) + minusbeta)) % len(alfabeto)]
        f = open("decrypt.aff","w",encoding="iso-8859-1")
        f.write(textoDescifrado)
        f.close
        return "Decipher made successfully, plese check your directory"
    except:
        return "Error Decryption"