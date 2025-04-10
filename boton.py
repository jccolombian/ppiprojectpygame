import pygame
pygame.font.init()

from ayudas import *

# variable para hacer un boton con bordes y de un color
'''
class boton:
    boton = None
    click = False
    texto = 'Click me'
    font = letra3
    fontSize = 20
    colorInactivo = color1
    colorActivo = color2
    colorTexto = color3
    coord = VECTOR(20,20)
    size = VECTOR(100,50)
    borde = False
'''

# variable para hacer un boton con un fondo de imagen
'''
class boton:
    boton = None
    click = False
    coord = VECTOR(20,20)
    size = VECTOR(100,50)
    imagen = pygame.image.load(poner imagen).convert_alpha()
'''

def activo(boton):
    pos = pygame.mouse.get_pos()
    if pos[0] > boton.boton.left and pos[0] < boton.boton.left + boton.size.x:
        if pos[1] > boton.boton.top and pos[1] < boton.boton.top + boton.size.y:
            return True
    return False    


def boton(boton):

    if boton.borde:
        boton.boton = pygame.draw.rect(
            ventana,
            negro,
            (boton.coord.x - 2,boton.coord.y - 2,boton.size.x + 4,boton.size.y + 4),
            0
        )
    else:
        pygame.draw.line(ventana,
                         blanco,
                         (boton.coord.x - 2,boton.coord.y - 2),
                         (boton.coord.x + boton.size.x,boton.coord.y - 2),
                         2)
            
        pygame.draw.line(ventana,
                         blanco,
                         (boton.coord.x - 2,boton.coord.y - 2),
                         (boton.coord.x - 2,boton.coord.y + boton.size.y),
                         2)
        
        pygame.draw.line(ventana,
                         negro,
                         (boton.coord.x,boton.coord.y + boton.size.y),
                         (boton.coord.x + boton.size.x,boton.coord.y + boton.size.y),
                         2)
        
        pygame.draw.line(ventana,
                         negro,
                         (boton.coord.x + boton.size.x,boton.coord.y),
                         (boton.coord.x + boton.size.x,boton.coord.y + boton.size.y),
                         2)

    boton.boton = pygame.draw.rect(
        ventana,
        boton.colorInactivo,
        (boton.coord.x,boton.coord.y,boton.size.x,boton.size.y),
        0
    )    

    if activo(boton):
        pygame.draw.rect(ventana,boton.colorActivo,boton.boton)
    else:
        pygame.draw.rect(ventana,boton.colorInactivo,boton.boton)    

    letra = pygame.font.SysFont(boton.font,boton.fontSize)
    contenido = letra.render(boton.texto,True,boton.colorTexto)
    ventana.blit(
        contenido,
        (boton.boton.left + (boton.size.x/2 - contenido.get_width()/2),
        boton.boton.top + (boton.size.y/2 - contenido.get_height()/2)
        )
    )

def click(boton):
    for evento in Ayudas.EVENTOS:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if activo(boton):
                boton.click = True
    return boton.click            

def botonImagen(boton):
    imagen = pygame.transform.scale(boton.imagen,(boton.size.x,boton.size.y))
    boton.boton = pygame.Surface((boton.size.x,boton.size.y))
    boton.boton.blit(imagen,(0,0))
    ventana.blit(boton.boton,(boton.coord.x,boton.coord.y))

def activoBotonImagen(boton):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if boton.boton.get_rect(topleft=(0, 0)).collidepoint(mouse_x, mouse_y):
        return True
    return False    

def clickBotonImagen(boton):
    for evento in Ayudas.EVENTOS:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if activoBotonImagen(boton):
                boton.click = not boton.click
    return boton.click  