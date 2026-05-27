# 1)  Importar la lista de pokemones del archivo heroes.py 
from pokemons import lista_pokemon
from app import *


def menu():
    mostrar_menu()
    opcion = comprobar_int('Ingrese alguna opcion: ')
    
    while opcion != 8: 
    #2) Listas todos los pokemones de una manera amena para el usuario 
        if opcion == 1:
            formatear_lista(lista_pokemon)
    #3) Agregar pokemon a la lista (se le pedirá todas las características de un pokemon al usuario y se agregará a la lista original) 
        elif opcion == 2:
            agregar_pokemon(lista_pokemon)
    #4)Eliminar pokémon  por nombre (el usuario ingresa un nombre y lo intenta eliminar de la lista) 
        elif opcion == 3:
            eliminar_pokemon(lista_pokemon)
    #5) Ordenar la lista de pokémons por nombre (alfabéticamente de la Z a la A) 
        elif opcion == 4:
            ordenar_lista(lista_pokemon)
    #6) Ver héroe más pesado de los de tipo agua (poder ver toda la información de manera amena para el usuario sobre el pokémon más pesado dentro de los de tipo agua) 
        elif opcion == 5:
            filtrar_mas_alto(lista_pokemon, PESO, 'Agua')
    #7) Ver pokemon con más fuerza de ataque (poder ver toda la información de manera amena para el usuario sobre el pokémon más fuerte) 
        elif opcion == 6:
            ver_mas_fuerte(lista_pokemon)
    #8) Listar sólo los pokemones de una región en particular de una manera amena para el usuario 
        elif opcion == 7:
            filtrar_por_region(lista_pokemon)
        else:
            opcion = comprobar_int('Opcion no valida, reingrese una opcion: ')
            while opcion <= 0 or opcion > 8:
                opcion = comprobar_int('Opcion no valida, reingrese una opcion: ')
        #Volver a mostar menu y elegir opcion
        mostrar_menu()  
        opcion = comprobar_int('Ingrese alguna opcion: ')

menu()
