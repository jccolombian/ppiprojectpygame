import pygame

from ayudas import *
from boton import *
from imagenes import *
from login import *

# zona de variables

class fondoInicio:
    size = VECTOR(ANCHO,ALTO)
    coord = VECTOR(0,0)
    archivo = pygame.image.load(summer).convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))

class explorador:
    size = VECTOR(100,150)
    coord = VECTOR(300,100)
    archivo = pygame.image.load(safari).convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))    

class titulo1:
    texto = 'Explorador del Futuro'
    size = 50
    color = yellow1
    font = letra6
    coord = VECTOR(70,300)


class botonSalir:
    boton = None
    click = False
    texto = 'Salir'
    font = letra3
    fontSize = 20
    colorInactivo = darkorange2
    colorActivo = tan1
    colorTexto = negro
    coord = VECTOR(650,50)
    size = VECTOR(100,50)
    borde = True    

class botonEntrar:
    boton = None
    click = False
    texto = 'Entrar'
    font = letra3
    fontSize = 20
    colorInactivo = darkorange2
    colorActivo = tan1
    colorTexto = negro
    coord = VECTOR(380,500)
    size = VECTOR(100,50)
    borde = True     

class mensajeIntermitente:
    texto = 'Explora tu ciudad'
    size = 30
    color = red
    font = letra5
    coord = VECTOR(300,400)
    parpadeando = True
    parpadear = pygame.USEREVENT + 1
    pygame.time.set_timer(parpadear,800)    

class textoTemporal1:
    texto = 'Hello'
    size = 50
    color = red
    font = letra4
    coord = VECTOR(10,10)
    inicio = pygame.time.get_ticks()
    tiempo = 100 #10segundos

# zona de funciones

def inicio():
    
    imagen(fondoInicio)
    imagen(explorador)
    mostrarTextoTTF(titulo1)
    boton(botonSalir)
    boton(botonEntrar)

    if click(botonSalir):
        pygame.quit()
        sys.exit()

    intermitenteTextoSistema(mensajeIntermitente)
    temporalTextoSystema(textoTemporal1)

    if click(botonEntrar):
        login()