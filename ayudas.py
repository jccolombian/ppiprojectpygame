import pygame, sys

from pygame.locals import *

pygame.init()

pygame.font.init()

FPS = 40

RELOJ = pygame.time.Clock()

ANCHO = 800

ALTO = 600

ventana = pygame.display.set_mode((ANCHO,ALTO))

pygame.display.set_caption('Aqui va el titulo de la ventana')

class Ayudas:
    pygame.init()
    EVENTOS = pygame.event.get()

# PALETA DE COLORES:
verdeGris = (224,238,224)
limon = '#EEE9BF'
slateblue4 = '#473C8B'
mediumseagreen = '#3CB371'
yellow1 = '#FFFF00'
darkgoldenrod4 = '#8B6508'
negro = (0,0,0)
blanco = (255,255,255)
springgreen = '#00FF7F'
springgreen3 = '#008B45'
cobaltgreen = '#3D9140'
darkorange2 = '#EE7600'
tan1 = '#FFA54F'
red = '#FF0000'


# TIPOS DE FUENTES:

letra1 = 'bahnschrift'

letra2 = 'papyrus'

letra3 = 'jokerman'

letra4 = 'frenchscript'

letra5 = 'stencil'

letra6 = './fonts/Anagram.ttf'

letra7 = './fonts/VT323-Regular.ttf'

# LISTA DE IMAGENES
grama = './imagenes/grama.png'
grama2 = './imagenes/grama2.png'
montaña = './imagenes/montaña.png'
nubes = './imagenes/nubes.png'
safari = './imagenes/safari.png'
summer = './imagenes/Summer5.png'

back = './imagenes/botones/back.png'
menu = './imagenes/botones/menu.png'
mfx = './imagenes/botones/mfx.png'
mfxs = './imagenes/botones/mfxs.png'
moregames = './imagenes/botones/moregames.png'

VECTOR = pygame.math.Vector2 


def mostrarLetraSistema():
    letras = pygame.font.get_fonts()
    for l in letras:
        print(l)

# variable texto normal:
'''
class texto:
    texto = 'Politécnico Colomibiano Jaime Isaza Cadavid'
    size = 50
    color = mediumseagreen
    font = letra4
    coord = VECTOR(50,50)
'''

# variable texto tipo parrafo:
'''
class texto:
    texto = ["Uno de los mayores anhelos después de cursar un programa académico en una institución",
             "universitaria, es culminar este ciclo con un acto de reconocimiento por parte de la institución al",
             "esfuerzo del estudiante, en el que le hace entrega formal del diploma que lo acredita como",
             "magíster, especialista, profesional, tecnólogo o técnico ñ."]
    size = 20
    color = darkgoldenrod4
    font = letra2
    coord = VECTOR(10,120)
'''

# variable texto normal efecto maquina de escribir:
'''
class texto:
    texto = 'Como animar texto con estilo de animación de maquina de escribir'
    size = 20
    color = slateblue4
    font = letra1
    coord = VECTOR(50,50)
    contador = 0
    velocidad = 3
'''

# variable texto tipo parrafo efecto maquina de escribir:
'''
class texto:
    texto = ["Uno de los mayores anhelos después de cursar un programa académico en una institución",
             "universitaria, es culminar este ciclo con un acto de reconocimiento por parte de la institución al",
             "esfuerzo del estudiante, en el que le hace entrega formal del diploma que lo acredita como",
             "magíster, especialista, profesional, tecnólogo o técnico ñ."]
    size = 20
    color = darkgoldenrod4
    font = letra2
    coord = VECTOR(10,120)
    contador = 0
    velocidad = 1
    actual = 0
    linea = texto[actual]
    listo = False
'''

def mostrarTextoSistema(texto):
    letra = pygame.font.SysFont(texto.font,texto.size)
    ventana.blit(letra.render(str(texto.texto),
                                  True,texto.color),
                                  (texto.coord.x,texto.coord.y))    

def mostrarTextoTTF(texto):
    letra = pygame.font.Font(texto.font,texto.size)
    ventana.blit(letra.render(str(texto.texto),
                                  True,texto.color),
                                  (texto.coord.x,texto.coord.y))  
    

def mostrarTextoLargoSistema(texto):
    letra = pygame.font.SysFont(texto.font,texto.size)
    y = texto.coord.y
    for linea in texto.texto:
        ventana.blit(letra.render(str(linea),
                                    True,texto.color),
                                    (texto.coord.x,y))
        y += 30        


def mostrarTextoSistemaMaquinaDeEscribir(texto):
    letra = pygame.font.SysFont(texto.font,texto.size)
    if texto.contador < texto.velocidad * len(texto.texto):
        texto.contador += 1
  
    ventana.blit(letra.render(str(texto.texto[0:texto.contador//texto.velocidad]),
                                  True,texto.color),
                                  (texto.coord.x,texto.coord.y))

 
def mostrarTextoLargoSistemaMaquinaDeEscribir(texto):
    letra = pygame.font.SysFont(texto.font,texto.size)

    if texto.contador < texto.velocidad * len(texto.linea):
        texto.contador += 1
    elif texto.contador >= texto.velocidad * len(texto.linea):
        texto.listo = True

    for evento in Ayudas.EVENTOS:
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RETURN and texto.listo and texto.actual < len(texto.texto)-1:
                texto.actual += 1
                texto.listo = False
                texto.linea = texto.texto[texto.actual]
                texto.contador = 0

    ventana.blit(letra.render(str(texto.linea[0:texto.contador//texto.velocidad]),
                                  True,texto.color),
                                  (texto.coord.x,texto.coord.y))
    
# variable texto que parpadea:
'''
class texto:
    texto = 'Politécnico Colomibiano Jaime Isaza Cadavid'
    size = 50
    color = mediumseagreen
    font = letra4
    coord = VECTOR(50,50)
    parpadeando = True
    parpadear = pygame.USEREVENT + 1
    pygame.time.set_timer(parpadear,800)
'''

def intermitenteTextoSistema(texto):
    for evento in Ayudas.EVENTOS:
        if evento.type == texto.parpadear:
            texto.parpadeando = not texto.parpadeando
    if texto.parpadeando:
        mostrarTextoSistema(texto)

def intermitenteTextoTTF(texto):
    for evento in Ayudas.EVENTOS:
        if evento.type == texto.parpadear:
            texto.parpadeando = not texto.parpadeando
    if texto.parpadeando:
        mostrarTextoTTF(texto)        

# variable texto que temporal:
'''
class texto:
    texto = 'Politécnico Colomibiano Jaime Isaza Cadavid'
    size = 50
    color = mediumseagreen
    font = letra4
    coord = VECTOR(50,50)
    inicio = pygame.time.get_ticks()
    tiempo = 1000 #10segundos
'''

def temporalTextoSystema(texto):
    segundos = (pygame.time.get_ticks() - texto.inicio)/texto.tiempo
    if segundos < texto.tiempo:
        mostrarTextoSistema(texto)

def temporalTextoTTF(texto):
    segundos = (pygame.time.get_ticks() - texto.inicio)/texto.tiempo
    if segundos < texto.tiempo:
        mostrarTextoTTF(texto)        