from django.http import HttpResponse
import matplotlib.pyplot as plt
import numpy as np
import math

#Función para simplificar la integración, esta función representa a la integral
def sustF(sigma,mi,x):
    return (1/(sigma*math.sqrt(2*math.pi)))*math.exp((-1/2)*pow((x-mi)/sigma,2))

#Funcion ocupada para graficar la funcion y el area bajo la curva obtenida
def Grafica(sigma,mi,area,a,b):
	
	f2 = np.vectorize(sustF)
	x = np.arange(a, b, 0.01)
	z = np.arange(a, b, 0.01)
	plt.plot(x, f2(sigma,mi,x))
	plt.fill_between(z, f2(sigma,mi,z), color='#539ecd')
	plt.grid()
	t1 = "Area bajo la curva del primer problema\n"
	t2 = "Area obtenida: %s"%(area)
	t1 = t1+t2+"u^2"
	plt.title(t1,fontsize=12)
	plt.savefig('Graficaproblema1.png', bbox_inches='tight')
	plt.show()
	return 0

#Programa Principal
def mainP(request,a,b,n,sigma,mi):
#Datos resividos y convertir a float
    a=float(a)
    b=float(b)
    n=float(n)
    sigma=float(sigma)
    mi=float(mi)
    aux = b
    auxa = a
    if(a>b):
        a=aux
        b=auxa
    #Resolviendo la integral
    dx=0
    suma=0
    dx = (b - a)/n #Delta de x
    suma = sustF(sigma,mi,a)+sustF(sigma,mi,b) #Primera suma
    i=1
    while i<n: 
        suma+=4*sustF(sigma,mi,a+i*dx)#Uno si otro no, por eso dos en dos
        #Ademas sustituimos en la original a + (ubicacion en n por ejemplo 1 multiplicado por la delta x)
        i+=2
    i=2
    while i<n:
        suma+=2*sustF(sigma,mi,a+i*dx)#Mismoo para 2 solo que incia en '2'
        #Ademas sustituimos en la original a + (ubicacion en n por ejemplo 2 multiplicado por la delta x)
        i+=2
    final = suma*dx/3#Siempre delta de x es dividida entre 3
    print("El valor de la integral evaluada esf: ", final)
    documento = "<html><head><title>Codigo</title><link rel='stylesheet' href='https://bulma.io/css/bulma-docs.min.css?v=201807271921'></head>"
    documento2="<body><p>El valor de la integral definida es: %s</p></body></html>" %(final)
    df = documento+documento2
    Grafica(sigma,mi,final,a,b)
    return HttpResponse(df)
