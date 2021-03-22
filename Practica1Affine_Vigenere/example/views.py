from django.shortcuts import render, redirect
from django.contrib import messages
from example.Vigenere import encrypt, decrypt
from example.Affine import Encrypt, Decrypt

def MainPage(request):
    return render(request, 'example/index.html')

def VigenerePage(request):
    return render(request, 'example/Vigenere.html')

def AffinePage(request):
    return render(request, 'example/Affine.html')

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

def CifrarAffine(request, filetxt, a, b, alphabet):
    message = Encrypt(filetxt,alphabet,int(a),int(b))
    if(len(message) <= 22):
        messages.add_message(request, messages.ERROR, message, extra_tags='CypherM')
    else:
        messages.add_message(request, messages.SUCCESS, message +', now you can go to decipher' , extra_tags='CypherM')
    return redirect('affine')

def DescifrarAffine(request, filetxt, a, b, alphabet):
    message = Decrypt(filetxt,alphabet,int(a),int(b))
    if(len(message) == 16):
        messages.add_message(request, messages.ERROR, message ,extra_tags='DecipherM')
    else:
        messages.add_message(request, messages.SUCCESS, message, extra_tags='DecipherM')
    return redirect('affine')