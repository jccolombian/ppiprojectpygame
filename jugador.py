import pygame

from pygame.sprite import Sprite

from ayudas import *

import math

'''
class Jugador:
    sprite = None
    imagen = './imagenes/.png'
    size = VECTOR((64,128))
    coord = VECTOR((32,64))
    velocidad = VECTOR((0,0))
    indice = 0
    movimientos = []
    saltando = False
    enTierra = True
    sonido_saltando = pygame.mixer.Sound('./audios/saltos/jump_10.wav')
'''  



def jugador(jugador):

    sprite = Sprite()

    imagen = pygame.image.load(jugador.imagen).convert_alpha()
    sprite.image = pygame.transform.scale(imagen,(jugador.size.x,jugador.size.y))
    sprite.rect = sprite.image.get_rect() 
    sprite.rect.x = jugador.coord.x
    sprite.rect.y = jugador.coord.y  

    jugador.sprite = sprite


def mover(jugador):

    variacion = VECTOR((0,0))

    teclas = pygame.key.get_pressed()

    if teclas[K_RIGHT]:
        variacion.x += 4 
        jugador.enTierra = True
        cargarAnimaciones(jugador,0)

    elif teclas[K_LEFT]:
        variacion.x -= 4
        jugador.enTierra = True
        cargarAnimaciones(jugador,1)

    elif Ayudas.ACCION == 'pausado_derecha':
        jugador.enTierra = True
        cargarAnimaciones(jugador,2)    

    elif Ayudas.ACCION == 'pausado_izquierda':
        jugador.enTierra = True
        cargarAnimaciones(jugador,3)   

    elif teclas[pygame.K_m]:
        if jugador.enTierra:
            jugador.sonido_saltando.play()
            jugador.velocidad.y = -12
            jugador.enTierra = False
            cargarAnimaciones(jugador,4)  

    elif teclas[pygame.K_z]:
        if jugador.enTierra:
            jugador.sonido_saltando.play()
            jugador.velocidad.y = -12  
            jugador.enTierra = False
            cargarAnimaciones(jugador,5)     

    
        
       
    jugador.velocidad.y += 1    
 
    if jugador.velocidad.y > 16:
        jugador.velocidad.y = 16

    variacion.y += jugador.velocidad.y    

    for plataforma in PLATAFORMAS:    
        # colision en x:
        if plataforma.rect.colliderect(jugador.sprite.rect.x + variacion.x,
                                       jugador.sprite.rect.y, 
                                       jugador.size.x,jugador.size.y):
            variacion.x = 0     

        # colision en y:          
        if plataforma.rect.colliderect(jugador.sprite.rect.x,
                                       jugador.sprite.rect.y+variacion.y, 
                                       jugador.size.x,jugador.size.y):
            # saltando y por debajo del suelo:
            if jugador.velocidad.y < 0:
                variacion.y = plataforma.rect.bottom-jugador.sprite.rect.top
                jugador.velocidad.y = 0
            # callendo y por encima del suelo:    
            elif jugador.velocidad.y >= 0:
                variacion.y = plataforma.rect.top-jugador.sprite.rect.bottom    
                jugador.velocidad.y = 0
                jugador.enTierra = False

    jugador.sprite.rect.x += variacion.x
    jugador.sprite.rect.y += variacion.y            

    if jugador.sprite.rect.bottom > ALTO:
        jugador.sprite.rect.y = ALTO-jugador.size.y
        variacion.y = 0

    if jugador.sprite.rect.left < 0:
        jugador.sprite.rect.x = ANCHO-jugador.size.x

    if jugador.sprite.rect.right > ANCHO:
        jugador.sprite.rect.x = 0    

    ventana.blit(jugador.sprite.image,jugador.sprite.rect)    
             

      

def cargarAnimaciones(jugador,animacion):
    animaciones = jugador.movimientos[animacion]
    jugador.indice = moverAnimaciones(animaciones,jugador.indice)
    jugador.sprite.image = animaciones[jugador.indice]     


def moverAnimaciones(animaciones,actual):

    if actual < len(animaciones)-1:
        actual += 1    
    else:
        actual = 0    

    return actual     

   
def moverIzquierdaDerecha(jugador,limiteIzquierdo,limiteDerecho):

    jugador.coord.x -= 1 * jugador.direccion

    if jugador.direccion > 0: 
        
        animaciones = jugador.movimientos[1]

        for event in Ayudas.EVENTOS:
            if event.type == jugador.VELOCIDAD_ANIMACIONES:
                if jugador.indice < len(animaciones)-1:
                    jugador.indice += 1    
                else:
                    jugador.indice = 0    

        jugador.sprite.image = animaciones[jugador.indice] 
    else:      
        animaciones = jugador.movimientos[0]
        
        for event in Ayudas.EVENTOS:
            if event.type == jugador.VELOCIDAD_ANIMACIONES:
                if jugador.indice < len(animaciones)-1:
                    jugador.indice += 1    
                else:
                    jugador.indice = 0   

        jugador.sprite.image = animaciones[jugador.indice] 

    if jugador.coord.x <= limiteIzquierdo:
        jugador.direccion *= -1

    if jugador.coord.x >= limiteDerecho:
        jugador.direccion *= -1
        
    jugador.sprite.rect.topleft = jugador.coord
           

def estanCerca(jugador1, jugador2,umbral):
    rect1 = jugador1.sprite.rect
    rect2 = jugador2.sprite.rect
    distancia = math.sqrt((rect1.centerx - rect2.centerx) ** 2 + (rect1.centery - rect2.centery) ** 2)
    
    if distancia < umbral and not rect1.colliderect(rect2):
        return True  
    return False           