import json
from random import randint
from PIL import Image

personajes = []
with open("parcial1-IA/personajes.json", "r") as file:
    personajes = json.load(file)

personaje_elegido = personajes[randint(0, len(personajes) - 1)]


def imprimir_personajes(personajes: list):

    for personaje in personajes:
        print(personaje["nombre"])
    print('')


def lista_atributos_personajes(personajes: list):
    atributos = list(personajes[0].keys())
    atributos.remove('nombre')
    atributos.remove('imagen')
    return atributos


def bienvenida(atributos: list):
    print("Bienvenid@ a una nueva partida de 'Adivina quién'. Tienes máximo 3 "
          "ayudas de los atributos del personaje para que puedas adivinar.\n")
    msj = 'Los comandos que se aceptan son: "adivinar", "listar", '
    cont = 1
    for atributo in atributos:
        if cont == len(atributos):
            msj += '\"' + atributo + '\" y '
        else:
            msj += '\"' + atributo + '\", '
        cont += 1
    msj += '"salir".\n'
    print(msj)


atributos = lista_atributos_personajes(personajes)
bienvenida(atributos)
print('Uno de estos personajes es el que debes adivinar: ')
imprimir_personajes(personajes)

comando_usuario = ''
estado_juego = ''
cantidad_preguntas = 3

while comando_usuario != 'salir' and estado_juego != 'terminado':

    if cantidad_preguntas > 0:

        comandos = ''
        for index in range(len(atributos)):
            comandos += atributos[index] + '/'
        if cantidad_preguntas == 1:
            print('¿Qué te gustaría realizar ó conocer del personaje?. (Te queda 1 ayuda)')
        else:
            print('¿Qué te gustaría realizar ó conocer del personaje?. Te quedan ' + str(cantidad_preguntas) + ' ayudas')
        comando_usuario = input('(adivinar/listar/' + comandos + 'salir): ')

        if comando_usuario.lower() == 'genero':
            print(personaje_elegido['genero'], '\n')
            cantidad_preguntas -= 1

        elif comando_usuario.lower() == 'edad':
            print(personaje_elegido['edad'], '\n')
            cantidad_preguntas -= 1

        elif comando_usuario.lower() == 'estatura':
            print(personaje_elegido['estatura'], '\n')
            cantidad_preguntas -= 1

        elif comando_usuario.lower() == 'cabello':
            print(personaje_elegido['cabello'], '\n')
            cantidad_preguntas -= 1

        elif comando_usuario.lower() == 'profesion':
            print(personaje_elegido['profesion'], '\n')
            cantidad_preguntas -= 1

        elif comando_usuario.lower() == 'lugar nacimiento':
            print(personaje_elegido['lugar nacimiento'], '\n')
            cantidad_preguntas -= 1

        elif comando_usuario.lower() == 'listar':
            print('lista de los personajes: ')
            print(imprimir_personajes(personajes))

        elif comando_usuario.lower() == 'adivinar':
            personaje_usuario = input(
                '¿Qué personaje crees que es?: ')
            estado_juego = 'terminado'

            if personaje_usuario.lower() == personaje_elegido['nombre'].lower():
                print("¡Felicitaciones! :) Haz adivinado el personaje\n")

                imagen = Image.open('parcial1-IA/images/' + personaje_elegido['imagen'])
                imagen.show()

            else:
                print("¡Rayos! :( Esta vez no haz logrado adivinar el personaje. El personaje era " +
                      personaje_elegido['nombre'], '\n')
                imagen = Image.open('parcial1-IA/images/over.jpg')
                imagen.show()

        elif comando_usuario.lower() == 'salir':
            estado_juego = 'terminado'

        else:
            print('Ingreso un comando no valido. intente nuevamente.\n')

    else:
        personaje_usuario = input(
            'Te has quedado sin ayudas. ¿Qué personaje crees que es?: ')
        estado_juego = 'terminado'

        if personaje_usuario.lower() == personaje_elegido['nombre'].lower():
            print("¡Felicitaciones! :) Haz adivinado el personaje\n")

            imagen = Image.open('parcial1-IA/images/' + personaje_elegido['imagen'])
            imagen.show()
            
        else:
            print("¡Rayos! :( Esta vez no haz logrado adivinar el personaje. El personaje era " +
                  personaje_elegido['nombre'], '\n')
            imagen = Image.open('parcial1-IA/images/over.jpg')
            imagen.show()
