from django.shortcuts import render, redirect
from django.contrib import messages
from example.Llaves import GenerateKeys
from example.RSA import cypher, decipher
from example.Vigenere import encrypt, decrypt


def MainPage(request):
    return render(request, 'example/index.html')

def CifrarVigenere(request, filetxt, key):
    message = encrypt(filetxt,key)
    if(len(message) == 13):
        messages.add_message(request, messages.ERROR, message+' wrong key', extra_tags='CypherM')
    else:
        messages.add_message(request, messages.SUCCESS, message +', now you can go to decipher' , extra_tags='CypherM')
    return redirect('vigenere')

def DescifrarVigenere(request, filetxt, key):
    message = decrypt(filetxt,key)
    if(len(message) == 16):
        messages.add_message(request, messages.ERROR, message+' wrong key',extra_tags='DecipherM')
    else:
        messages.add_message(request, messages.SUCCESS, message, extra_tags='DecipherM')
    return redirect('vigenere')

def VigenerePage(request):
    return render(request, 'example/Vigenere.html')

def DescifrarPage(request):
    return render(request, 'example/Descifrado.html')

def CifrarTxt(request, filetxt, privatekey):
    message = cypher(filetxt,privatekey)
    messages.add_message(request, messages.SUCCESS, message)
    return redirect('cypher')

def DescifrarTxt(request, filetxt, privatekey):
    message = decipher(filetxt,privatekey)
    #Manejo de error
    if(len(message) == 16):
        messages.add_message(request, messages.ERROR, message+' wrong private key')
    else:
        messages.add_message(request, messages.SUCCESS, message)

    return redirect('descipher')
