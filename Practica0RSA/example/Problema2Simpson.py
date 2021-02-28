from django.http import HttpResponse
import reportlab.platypus as platypus
from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, PageBreak, PageTemplate,NextPageTemplate, Image
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY,TA_CENTER
from reportlab.lib.units import inch
from numpy import array
import math
import os

#Función para simplificar la integración, esta función representa a la integral
def sustF(x):
    return (1/math.sqrt(2*math.pi))*math.exp((-1/2)*pow(x,2))

#Función para generar el PDF de las soluciones
def GeneraPDF(t,arreglo):
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    pa = "%s"%(desktop)
    pa = pa + "/Resultados.pdf"
    doc = BaseDocTemplate(pa,showBoundary=1)
    story = []
    t-=1
    nc = 0
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    logo = "Banner.png"
    #Portada
    im = Image(logo, doc.width - .25*inch, 1.65*inch)
    story.append(im)
    story.append(Paragraph("Instituto Politecnico Nacional", styles["Center"]))
    story.append(Paragraph("Escuela Superior de Computo", styles["Center"]))
    story.append(Paragraph("Probabilidad y Estadistica", styles["Center"]))
    story.append(Paragraph("Resultados de la integral definida en diferentes intervalos", styles["Center"]))
    story.append(Paragraph("Nombre de los alumnos:", styles["Justify"]))
    story.append(Paragraph("    -Cabrera Salinas Uriel / No de lista: 7/Correo: ", styles["Justify"]))
    story.append(Paragraph("    -Martinez Coronel Brayan Yosafat / No de lista: 19/ Correo: yosafatmartinez21@gmail.com", styles["Justify"]))
    story.append(Paragraph("    -Nevarez Tovar Juan Carlos / No de lista: 6/Correo: juan.nevtor@hotmail.com", styles["Justify"]))
    story.append(Paragraph("    -Ramirez Olvera Guillermo / No de lista: 10/Correo : memo0p2@hotmail.com", styles["Justify"]))
    story.append(Paragraph("    -Sanchez Mendez Edmundo Josue / No de lista: 20 /Correo: edmundoelpro1@gmail.com", styles["Justify"]))
    story.append(Paragraph("Nombre del profesor: Montiel Sanchez Angel Salvador /Correo: chavamontiel1@hotmail.com", styles["Justify"]))
    story.append(Paragraph("Grupo: 2CM8", styles["Justify"]))
    story.append(NextPageTemplate('Col'))
    story.append(PageBreak())
    #Medidad de las columnas
    frameCount = 3
    frameWidth = doc.width/frameCount
    frameHeight = doc.height-.05*inch
    frameT = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
    frames = []
    #Se crea un frame y se añade, con base en las columnas
    for frame in range(frameCount):
        leftMargin = doc.leftMargin + frame*frameWidth

        column = platypus.Frame(leftMargin, doc.bottomMargin, frameWidth, frameHeight)
        frames.append(column)
    template = platypus.PageTemplate(id='Col',frames=frames)
    #Resultados
    while(t>=0):
        story.append(Paragraph(arreglo[t], styles['Normal']))
        #print(arreglo[t])
        t-=1
        #if(nc==223):
            #story.append(PageBreak())
          #  nc=-1
        #nc+=1
    doc.addPageTemplates([PageTemplate(id='OneCol',frames=frameT),template])
    doc.build(story)

    return 0

#Programa Principal
def mainPP(request,n):
    #Pidiendo datos
    a = -6
    b = -5.99
    n = float(n)
    t=0;
    arreglo=[]
    #Variando el limite superior desde -5.99 hasta 6 con un cambio de 0.01
    while(b<=6):
        #Resolviendo la integral
        dx = (b - a)/n #Delta de x
        suma = sustF(a)+sustF(b) #Primera suma
        i=1
        while i<n: 
            suma+=4*sustF(a+i*dx)#Uno si otro no, por eso dos en dos
            #Ademas sustituimos en la original a + (ubicacion en n por ejemplo 1 multiplicado por la delta x)
            i+=2
        i=2
        while i<n:
            suma+=2*sustF(a+i*dx)#Mismoo para 2 solo que incia en '2'
            #Ademas sustituimos en la original a + (ubicacion en n por ejemplo 2 multiplicado por la delta x)
            i+=2
        final = suma*dx/3#Siempre delta de x es dividida entre 3
        print("El valor de la integral evaluada de ", a, " a ", b," es: ", final)
        t+=1
        sf = str(final)
        r = "%s"%(a)
        rr = " a %s"%(round(b, 4))
         
        if (sf.count('e')>=1):
            r = r + rr + " = %s"%(sf[0:8]+sf[len(sf)-4:len(sf)])
        else:
            if (b==-8.362407988293796e-14):
               r = "-6 a 0.0 = 0.5" 
            else:
                r = r + rr + " = %s"%(sf[0:12])
        arreglo.append(r)
        b +=0.01
    GeneraPDF(t,arreglo)
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    pa = "%s"%(desktop)
    pa = pa + "/Resultados.pdf"
    documento = "<html><head><title>Codigo</title><link rel='stylesheet' href='https://bulma.io/css/bulma-docs.min.css?v=201807271921'></head>"
    documento2="<body><p>Copie lo que esta en azul en su navegador para ver el pdf</p><a href=''><p>%s</p></a></body></html>"%(pa)
    return HttpResponse(documento+documento2)
