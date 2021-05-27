from django.shortcuts import render, redirect
from django.contrib import messages
from example.firma import signature, validate
def MainPage(request):
    return render(request, 'example/index.html')

def FimaDigitalPage(request):
    return render(request, 'example/FimaDigital.html')

def Firmar(request, msgfile, pkfile):
    message = signature(msgfile, pkfile)
    if(len(message) == 24):
        messages.add_message(request, messages.SUCCESS, message, extra_tags='Firma_txt')
    else:
        messages.add_message(request, messages.ERROR, message, extra_tags='Firma_txt')
    return redirect('ds')
    
def Validar(request, msgfile, pkfile):
    message = validate(msgfile, pkfile)
    print(len(message))
    if(len(message) == 19):
        messages.add_message(request, messages.SUCCESS, message , extra_tags='Validate_txt')
    else:
        messages.add_message(request, messages.ERROR, message, extra_tags='Validate_txt')
    return redirect('ds')
