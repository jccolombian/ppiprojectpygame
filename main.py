import pygame, sys

from ayudas import *
from boton import *
from entradadetexto import *
from inicio import *

# zona de variables
class texto1:
    texto = 'Politécnico Colomibiano Jaime Isaza Cadavid'
    size = 50
    color = mediumseagreen
    font = letra4
    coord = VECTOR(50,50)


class texto2:
    texto = 'Hoy juega la Selección y va a ganar'
    size = 30
    color = darkgoldenrod4
    font = letra7
    coord = VECTOR(50,120)


class texto3:
    texto = ["Uno de los mayores anhelos después de cursar un programa académico en una institución",
             "universitaria, es culminar este ciclo con un acto de reconocimiento por parte de la institución al",
             "esfuerzo del estudiante, en el que le hace entrega formal del diploma que lo acredita como",
             "magíster, especialista, profesional, tecnólogo o técnico ñ."]
    size = 20
    color = darkgoldenrod4
    font = letra2
    coord = VECTOR(10,120)


class texto4:
    texto = 'Como animar texto con estilo de animación de maquina de escribir'
    size = 20
    color = slateblue4
    font = letra1
    coord = VECTOR(50,50)
    contador = 0
    velocidad = 3

class texto5:
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

class boton1:
    boton = None
    click = False
    texto = 'Click me'
    font = letra3
    fontSize = 20
    colorInactivo = springgreen3
    colorActivo = springgreen
    colorTexto = blanco
    coord = VECTOR(20,20)
    size = VECTOR(100,50)
    borde = False

class entradadetexto1:
    entrada = None
    click = False
    texto = ''
    cursor = True
    font = letra4
    fontSize = 20
    colorInactivo = negro
    colorActivo = springgreen3
    eventoCursor = pygame.USEREVENT + 1
    pygame.time.set_timer(eventoCursor,500)
    coord = VECTOR(200,100)
    size = VECTOR(200,50)

class entradadetexto2:
    entrada = None
    click = False
    texto = ''
    cursor = True
    font = letra4
    fontSize = 20
    colorInactivo = negro
    colorActivo = springgreen3
    eventoCursor = pygame.USEREVENT + 1
    pygame.time.set_timer(eventoCursor,500)
    coord = VECTOR(200,200)
    size = VECTOR(200,50)

# zona de funciones
    




if __name__ == '__main__':

    while True:

        Ayudas.EVENTOS = pygame.event.get()

        for evento in Ayudas.EVENTOS:

            if evento.type == QUIT or (evento.type == KEYDOWN and evento.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        ventana.fill(verdeGris)

        #mostrarTextoSistema(texto1)

        #mostrarTextoTTF(texto2)

        #mostrarTextoLargoSistema(texto3)

        #mostrarTextoSistemaMaquinaDeEscribir(texto4)

        #mostrarTextoLargoSistemaMaquinaDeEscribir(texto5)
        
        #boton(boton1)
        #print(click(boton1))

        #entrada(entradadetexto1)

        #entrada(entradadetexto2)

        '''
        if click(boton1):
            print(entradadetexto2.texto)
            boton1.click = False
            resetear(entradadetexto2)'
        '''

        inicio()

        pygame.display.update()
        RELOJ.tick(FPS)