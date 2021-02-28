from django.shortcuts import render, redirect
from django.contrib import messages
from example.Llaves import GenerateKeys
from example.RSA import cypher, decipher

def MainPage(request):
    return render(request, 'example/index.html')

def GetKeys(request):
    GenerateKeys()
    messages.add_message(request, messages.SUCCESS, 'Keys generated successfully')
    return redirect('index')

def CifradoPage(request):
    return render(request, 'example/Cifrado.html')

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
