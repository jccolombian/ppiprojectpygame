import pygame

from ayudas import *
from imagenes import *
from boton import *
from login import login

# zona de variables

class fondo:
    size = VECTOR(ANCHO,ALTO)
    coord = VECTOR(0,0)
    archivo = pygame.image.load(summer).convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))

class logo:
    size = VECTOR(300,180)
    coord = VECTOR(250,50)
    archivo = pygame.image.load(logo).convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))


class titulo:
    texto = 'Exploremos con Luis Norberto'
    size = 25
    color = red
    font = letra6
    coord = VECTOR(250,260)
    contador = 0
    velocidad = 3    

class texto2:
    texto = 'Vamos a almorzar'
    size = 50
    color = mediumseagreen
    font = letra4
    coord = VECTOR(250,305)
    parpadeando = True
    parpadear = pygame.USEREVENT + 1
    pygame.time.set_timer(parpadear,800)


class cerrar:
    boton = None
    click = False
    texto = 'Salir'
    font = letra3
    fontSize = 15
    colorInactivo = hotpink3
    colorActivo = hotpink
    colorTexto = blanco
    coord = VECTOR(650,20)
    size = VECTOR(80,30)
    borde = True


class jugar:
    boton = None
    click = False
    texto = 'Jugar'
    font = letra3
    fontSize = 20
    colorInactivo = hotpink3
    colorActivo = hotpink
    colorTexto = blanco
    coord = VECTOR(350,450)
    size = VECTOR(100,50)
    borde = True

# zona de funciones



def inicio():

    

    imagen(fondo)
    imagen(logo)
    mostrarTextoTTFMaquinaDeEscribir(titulo)
    intermitenteTextoSistema(texto2)
    boton(cerrar)
    boton(jugar)

    if click(cerrar):
        pygame.quit()
        sys.exit()
      

    if click(jugar): 
        Ayudas.actual = 'login'
        jugar.click = False
        
        
    


