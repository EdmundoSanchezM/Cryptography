from django.shortcuts import render, redirect
from django.contrib import messages
from example.AES import encrypt_CBC,encrypt_CFB,encrypt_ECB,encrypt_OFB,decrypt_ECB,decrypt_CBC,decrypt_CFB,decrypt_OFB

def MainPage(request):
    return render(request, 'example/index.html')

def AESPage(request):
    return render(request, 'example/AES.html')

def CifrarAES(request, opcion, imgfile, password, initvector):
    message = ""
    if(int(opcion) == 0):
        message = encrypt_ECB(password, imgfile)
    elif(int(opcion) == 1):
        message = encrypt_CBC(password, initvector, imgfile)
    elif(int(opcion) == 2):
        message = encrypt_CFB(password, initvector, imgfile)
    elif(int(opcion) == 3):
        message = encrypt_OFB(password, initvector, imgfile)
    if(len(message) == 20):
        messages.add_message(request, messages.ERROR, message, extra_tags='CypherM')
    else:
        messages.add_message(request, messages.SUCCESS, message +', now you can go to decipher' , extra_tags='CypherM')
    return redirect('aes')
    
def DescifrarAES(request, opcion, imgfile, password, initvector):
    message = ""
    if(int(opcion) == 0):
        message = decrypt_ECB(password, imgfile)
    elif(int(opcion) == 1):
        message = decrypt_CBC(password, initvector, imgfile)
    elif(int(opcion) == 2):
        message = decrypt_CFB(password, initvector, imgfile)
    elif(int(opcion) == 3):
        message = decrypt_OFB(password, initvector, imgfile)
    if(len(message) == 20):
        messages.add_message(request, messages.ERROR, message, extra_tags='DecipherM')
    else:
        messages.add_message(request, messages.SUCCESS, message , extra_tags='DecipherM')
    return redirect('aes')
