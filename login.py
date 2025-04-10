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


class logo:
    size = VECTOR(200,300)
    coord = VECTOR(10,10)
    archivo = pygame.image.load(safari).convert_alpha()
    imagen = pygame.transform.scale(archivo,(size.x,size.y))


class titulo:
    texto = 'Exploremos el Mundo'
    size = 60
    color = orange2
    font = letra2
    coord = VECTOR(200,100)

class textoUsuario:
    texto = 'Usuario:'
    size = 30
    color = orange2
    font = letraSistema6
    coord = VECTOR(200,300)


class textoPassword:
    texto = 'Password:'
    size = 30
    color = orange2
    font = letraSistema6
    coord = VECTOR(200,370)


class ingresarUsuario:
    entrada = None
    click = False
    texto = ''
    cursor = True
    font = letraSistema6
    fontSize = 20
    colorInactivo = orange2
    colorActivo = springgreen3
    eventoCursor = pygame.USEREVENT + 1
    pygame.time.set_timer(eventoCursor,500)
    coord = VECTOR(330,290)
    size = VECTOR(200,50)
    password = False

class ingresarPassword:
    entrada = None
    click = False
    texto = ''
    cursor = True
    font = letraSistema6
    fontSize = 20
    colorInactivo = orange2
    colorActivo = springgreen3
    eventoCursor = pygame.USEREVENT + 1
    pygame.time.set_timer(eventoCursor,500)
    coord = VECTOR(330,360)
    size = VECTOR(200,50)
    password = False

class botonJugar:
    boton = None
    click = False
    texto = 'Jugar'
    font = letra3
    fontSize = 20
    colorInactivo = orange2
    colorActivo = yellow1
    colorTexto = blanco
    coord = VECTOR(200,430)
    size = VECTOR(150,50)
    borde = False


class botonRegistrarse:
    boton = None
    click = False
    texto = 'Registrarse'
    font = letra3
    fontSize = 20
    colorInactivo = orange2
    colorActivo = yellow1
    colorTexto = blanco
    coord = VECTOR(200,500)
    size = VECTOR(150,50)
    borde = False

class errorUsuario:
    texto = ''
    size = 50
    color = red
    font = letra4
    coord = VECTOR(330,290)
    inicio = pygame.time.get_ticks()
    tiempo = 500 #10segundos

class errorPassword:
    texto = ''
    size = 50
    color = red
    font = letra4
    coord = VECTOR(330,360)
    inicio = pygame.time.get_ticks()
    tiempo = 500 #10segundos


class botonAceptarErrores:
    boton = None
    click = False
    texto = 'Aceptar'
    font = letra3
    fontSize = 20
    colorInactivo = orange2
    colorActivo = yellow1
    colorTexto = blanco
    coord = VECTOR(400,430)
    size = VECTOR(0,50)
    borde = False


class password:
    entrada = None
    click = False
    texto = ''
    cursor = True
    font = letraSistema6
    fontSize = 20
    colorInactivo = orange2
    colorActivo = springgreen3
    eventoCursor = pygame.USEREVENT + 1
    pygame.time.set_timer(eventoCursor,500)
    coord = VECTOR(400,500)
    size = VECTOR(150,50)
    password = True

def login():
    imagen(fondoLogin)
    imagen(logo)

    mostrarTextoSistema(titulo)
    mostrarTextoSistema(textoUsuario)
    mostrarTextoSistema(textoPassword)

    entrada(ingresarUsuario)
    entrada(ingresarPassword)
    entrada(password)

    boton(botonJugar)
    boton(botonRegistrarse)

    
    


    boton(botonAceptarErrores)
    

    if click(botonJugar):

        errores = False

        if ingresarUsuario.texto == "":
            errorUsuario.texto = "Ingrese el usuario"
            mostrarTextoSistema(errorUsuario)
            errores = True
            

        if ingresarPassword.texto == "":
            errorPassword.texto = "Ingrese el password"
            mostrarTextoSistema(errorPassword)
            errores = True
                
        if errores:
            botonAceptarErrores.size.x = 150

        if not errores:
            print(ingresarUsuario.texto)
            print(ingresarPassword.texto)
            print(password.texto)
            resetear(ingresarUsuario)
            resetear(ingresarPassword)
            resetear(password)
            
    

    if click(botonAceptarErrores):
        errorUsuario.texto = ''
        errorPassword.texto = ''
        botonAceptarErrores.size.x = 0
