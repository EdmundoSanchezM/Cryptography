from math import floor
import random
import os
script_dir = os.path.dirname(__file__) 

def mcd(a, b):
    if b == 0:
        return a
    return mcd(b,a%b)

def generateRandom(longitud):
    m = []
    for i in range(1,longitud):
        m.append(i)
    maux = []
    for i in m:
        if(mcd(i,longitud)==1):
            maux.append(i)
    return random.choice(maux),random.randint(0,longitud)

def euclides(divisor, dividendo):
    inverso = True
    gx = divisor
    gy = dividendo
    u1 = 1
    u2 = 0
    v1 = 0
    v2 = 1
    u = 0
    v = 1
    while(dividendo != 0):
        q = floor(divisor / dividendo)
        r = divisor % dividendo
        divisor = dividendo
        dividendo = r
        if (r != 0):
            u = u1 - q * u2
            v = v1 - q * v2
            u1 = u2
            v1 = v2
            u2 = u
            v2 = v
    sv = v
    if (sv < 0):
        sv = gx + sv
    if(inverso):
        return sv
    else:
        return divisor

def Encrypt(archivo, alphabet, alpha, beta):
    f=open(archivo,"r")
    texto=f.read()
    f.close()
    mensaje = "Cypher made successfully plese check your directory"
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    bandera = True
    if ',' in alphabet:
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
    if(mcd(alpha,len(alfabeto))==1 and alpha<len(alfabeto)):
        textoCifrado = ""
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
        if ',' in alphabet:
            alfabeto = alphabet.replace(',', '')
        elif alphabet == "ES":
            alfabeto = "abcdefghijklmnñopqrstuvwxyz "
        elif alphabet == "D":
            alfabeto= "0123456789"
        elif alphabet == "ASCII":
            alfabeto = [chr(i) for i in range(256)]
            bandera = False
        inversoalpha = euclides(len(alfabeto),alpha)
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

def main():
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    print("Ingrese a (multiplicador)")
    a=int(input())
    print("Ingrese b (aditivo)")
    b=int(input())
    if(mcd(a,len(alfabeto))==1 and a<len(alfabeto)):
        inverso = euclides(len(alfabeto),a)
        print("El inverso multiplicativo de "+str(a)+" es: "+str(inverso))
        e = Encrypt("cryptographyclass", alfabeto,a,b)
        xd = InversoAditivo(b,len(alfabeto))
        #inverso = pow(a, -1, len(alfabeto))
        d = Decrypt(e,alfabeto,inverso, xd)
        print(e)
        print(d)
    else:
        print("Llave no valida\nRecuerde que a y la longitud del alfabeto deben ser primos relativos")
#Como precondiciones esta que el usuario haya selecionado un alfabeto