import pygame

from ayudas import *
from boton import *
from imagenes import *
from entradadetexto import *

class fondoLogin:
    size = VECTOR(ANCHO,ALTO)
    coord = VECTOR(0,0)
    archivo = pygame.image.load(nubes).convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))

class botonOpciones:
    boton = None
    click = False
    coord = VECTOR(20,20)
    size = VECTOR(50,50)
    imagen = pygame.image.load(moregames).convert_alpha()


def login():
    imagen(fondoLogin)
    botonImagen(botonOpciones)

    if clickBotonImagen(botonOpciones):
        print('Yes')
        botonOpciones.click = False