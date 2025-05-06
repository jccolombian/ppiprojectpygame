import pygame

from pygame.sprite import Sprite

from jugador import *

class pepito:
    sprite = None
    imagen = './imagenes/jugador1/idle/1.png'
    size = VECTOR((40,80))
    coord = VECTOR((10,10))
    velocidad = VECTOR((0,0))
    indice = 0
    movimientos = []
    saltando = False
    enTierra = False
    sonido_saltando = salto

jugador(pepito)

ancho_idle = 40
alto_idle = 80
ancho_derecha = 60 
alto_derecha = 75
ancho_salto = 40
alto_salto = 75

caminar_derecha = []

# caminar_derecha:

caminar_derecha.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/jugador1/derecha/1.png'),
        (ancho_derecha,alto_derecha)
    )
)
caminar_derecha.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/jugador1/derecha/2.png'),
        (ancho_derecha,alto_derecha)
    )
)
caminar_derecha.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/jugador1/derecha/3.png'),
        (ancho_derecha,alto_derecha)
    )
)
caminar_derecha.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/jugador1/derecha/4.png'),
        (ancho_derecha,alto_derecha)
    )
)
caminar_derecha.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/jugador1/derecha/5.png'),
        (ancho_derecha,alto_derecha)
    )
)
caminar_derecha.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/jugador1/derecha/6.png'),
        (ancho_derecha,alto_derecha)
    )
)
caminar_derecha.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/jugador1/derecha/7.png'),
        (ancho_derecha,alto_derecha)
    )
)
caminar_derecha.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/jugador1/derecha/8.png'),
        (ancho_derecha,alto_derecha)
    )
)

pepito.movimientos.append(caminar_derecha) # indice 0

caminar_izquierda = []

# caminar_izquierda
for sprite in caminar_derecha:
    caminar_izquierda.append(pygame.transform.flip(sprite,True,False))#imagen,horizontal,vertical

pepito.movimientos.append(caminar_izquierda) # 1


# Inactivo derecha:

inactivo_derecha = []

inactivo_derecha.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/jugador1/idle/1.png'),
        (ancho_idle,alto_idle)
    )
)
inactivo_derecha.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/jugador1/idle/2.png'),
        (ancho_idle,alto_idle)
    )
)
inactivo_derecha.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/jugador1/idle/3.png'),
        (ancho_idle,alto_idle)
    )
)
inactivo_derecha.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/jugador1/idle/4.png'),
        (ancho_idle,alto_idle)
    )
)
inactivo_derecha.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/jugador1/idle/5.png'),
        (ancho_idle,alto_idle)
    )
)
inactivo_derecha.append(
    pygame.transform.scale(
        pygame.image.load('./imagenes/jugador1/idle/6.png'),
        (ancho_idle,alto_idle)
    )
)

pepito.movimientos.append(inactivo_derecha) # 2


# Inactivo izquierda:

inactivo_izquierda = []

for sprite in inactivo_derecha:
    inactivo_izquierda.append(pygame.transform.flip(sprite,True,False))#imagen,horizontal,vertical

pepito.movimientos.append(inactivo_izquierda) # 3

# saltar_derecha:
saltar_derecha = []

saltar_derecha.append(
    pygame.transform.scale(pygame.image.load('./imagenes/jugador1/salto/1.png'),(ancho_salto,alto_salto))
) 
saltar_derecha.append(
    pygame.transform.scale(pygame.image.load('./imagenes/jugador1/salto/2.png'),(ancho_salto,alto_salto))
)  
saltar_derecha.append(
    pygame.transform.scale(pygame.image.load('./imagenes/jugador1/salto/3.png'),(ancho_salto,alto_salto))
)
saltar_derecha.append(
    pygame.transform.scale(pygame.image.load('./imagenes/jugador1/salto/4.png'),(ancho_salto,alto_salto))
)  
saltar_derecha.append(
    pygame.transform.scale(pygame.image.load('./imagenes/jugador1/salto/5.png'),(ancho_salto,alto_salto))
) 
saltar_derecha.append(
    pygame.transform.scale(pygame.image.load('./imagenes/jugador1/salto/6.png'),(ancho_salto,alto_salto))
) 
saltar_derecha.append(
    pygame.transform.scale(pygame.image.load('./imagenes/jugador1/salto/7.png'),(ancho_salto,alto_salto))
) 
saltar_derecha.append(
    pygame.transform.scale(pygame.image.load('./imagenes/jugador1/salto/8.png'),(ancho_salto,alto_salto))
) 
saltar_derecha.append(
    pygame.transform.scale(pygame.image.load('./imagenes/jugador1/salto/9.png'),(ancho_salto,alto_salto))
) 
saltar_derecha.append(
    pygame.transform.scale(pygame.image.load('./imagenes/jugador1/salto/10.png'),(ancho_salto,alto_salto))
) 
saltar_derecha.append(
    pygame.transform.scale(pygame.image.load('./imagenes/jugador1/salto/11.png'),(ancho_salto,alto_salto))
) 
saltar_derecha.append(
    pygame.transform.scale(pygame.image.load('./imagenes/jugador1/salto/12.png'),(ancho_salto,alto_salto))
) 
pepito.movimientos.append(saltar_derecha) # 4

# saltar izquierda:

saltar_izquierda = []

for sprite in saltar_derecha:
    saltar_izquierda.append(pygame.transform.flip(sprite,True,False))#imagen,horizontal,vertical

pepito.movimientos.append(saltar_izquierda) # 5

