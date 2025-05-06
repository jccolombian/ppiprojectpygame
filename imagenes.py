import pygame

from ayudas import *

pygame.font.init()

'''
class imagen:
    size = VECTOR(100,100)
    coord = VECTOR(10,10)
    archivo = pygame.image.load('variableImagen').convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))
    posicion = 0
'''

def imagen(imagen):
    ventana.blit(imagen.imagen,imagen.imagen.get_rect(topleft = (imagen.coord.x,imagen.coord.y)))

def desplazarFondo(fondo):

    ventana.blit(fondo.imagen,(fondo.posicion,0))

    ventana.blit(fondo.imagen,(fondo.size.x + fondo.posicion,0))       

    fondo.posicion -= 3

    if abs(fondo.posicion) > fondo.size.x:
        fondo.posicion = 0