from math import floor

def Convert(string): 
    list1=[] 
    list1[:0]=string 
    return list1

def mcd(a, b):
    if b == 0:
        return a
    return mcd(b,a%b)

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

def Encrypt(texto, alfabeto, alpha, beta):
    textoCifrado = ""
    for p in texto:
        textoCifrado += alfabeto[((alpha * alfabeto.find(p) )+ beta) % len(alfabeto)]
    return textoCifrado

def InversoAditivo(beta,n):
    return int(n-beta)

def Decrypt(textoCifrado, alfabeto, inversoalpha, minusbeta):
    textoDescifrado = ""
    for c in textoCifrado:
        textoDescifrado += alfabeto[ (inversoalpha * (alfabeto.find(c) + minusbeta)) % len(alfabeto)]
    return textoDescifrado

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
main()