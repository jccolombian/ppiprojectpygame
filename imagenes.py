import pygame

from ayudas import *

pygame.font.init()

'''
class imagen:
    size = VECTOR(100,100)
    coord = VECTOR(10,10)
    archivo = pygame.image.load('variableImagen').convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))
'''

def imagen(imagen):
    ventana.blit(imagen.imagen,imagen.imagen.get_rect(topleft = (imagen.coord.x,imagen.coord.y)))
