# 1)  Importar la lista de pokemones del archivo heroes.py 
from pokemons import lista_pokemon

'''
Enunciado/s: 
    La Liga Pokémon abrió nuevas vacantes para entrenadores e investigadores especializados en análisis de datos. Para ingresar al laboratorio principal, los candidatos deberán resolver una serie de desafíos de programación. 
    
    El profesor Oak compartió información confidencial de distintos Pokémon registrados en la Pokédex. Cada Pokémon posee datos como nombre, tipo, altura, peso, nivel, puntos de ataque y región de origen. 
    
    El objetivo será resolver los requerimientos que nos soliciten. Los mejores participantes podrán formar parte del equipo oficial de investigación Pokémon. Nos pidieron hacer una aplicación con un menú que contenga las siguientes opciones:

Consignas 

Objetivos de Aprobación Directa (Calificación de 6 a 10 puntos): 
    ● Integración de todos los temas vistos en clase hasta el momento del parcial, sin usar librerías ni recursos externos 
    ● Que todas las opciones funcionen de manera correcta y el código este escrito siguiendo todas las buenas prácticas de la programación 
    ● Poder defender con lenguaje fluido y técnico el entregable 
'''

#2) Listas todos los pokemones de una manera amena para el usuario 
def formatear_lista(lista: list):
    
    print(f'\nDatos de los pokemones: ')
    for i in range(len(lista)):
        print(f'\n Nombre: {lista[i][0]} \n Tipo: {lista[i][1]} \n Altura: {lista[i][2]} mts \n Peso: {lista[i][3]} kg \
            \n Nivel: {lista[i][4]} \n Fuerza: {lista[i][5]} \n Region: {lista[i][6]} \n')



#3) Agregar pokemon a la lista (se le pedirá todas las características de un pokemon al usuario y se agregará a la lista original) 
def comprobar_str(texto: str) -> str:
    dato = input(texto)

    while dato == '':
        dato = input('Dato invalido, deber ser un texto y no puede estar vacio: ')
    return dato


def comprobar_int(texto: str) -> int:
    dato = int(input(texto))

    while dato <= 0:
        dato = int(input('Dato invalido, debe ingresar un numero entero y mayor a 0: '))

    return dato

def comprobar_region() -> str:
        region = comprobar_str('Ingrese la region de su pokemon: ')
        
        while region != 'Johto' and region != 'Kanto' and region != 'Sinnoh' and region != 'Hoenn':
            region = comprobar_str('Ingrese la region de su pokemon: ')
        
        return region

def agregar_pokemon(lista: list):
    nombre = comprobar_str('Ingrese el nombre de su pokemon: ')
    tipo = comprobar_str('Ingrese el tipo de su pokemon: ')
    nivel = comprobar_int('Ingrese el nivel de su pokemon: ')
    peso = comprobar_int('Ingrese el peso de su pokemon: ')
    altura = comprobar_int('Ingrese la altura de su pokemon: ')
    fuerza_ataque = comprobar_int('Ingrese la fuerza de su pokemon: ')
    region = comprobar_region()

    nuevo_pokemon = [nombre, tipo, nivel, peso, altura, fuerza_ataque, region]

    lista.append(nuevo_pokemon)

    print(f'\nPokemon agregado: {nuevo_pokemon[0]}!')
    formatear_lista(lista)

#4)Eliminar pokémon  por nombre (el usuario ingresa un nombre y lo intenta eliminar de la lista) 
def eliminar_pokemon(lista: list):
    formatear_lista(lista)
    nombre = comprobar_str('Ingrese el nombre del pokemon que desea eliminar: ')
    for i in range(len(lista)):
        if lista[i][0] == nombre:
            lista.pop(i)
            break

    print(f'El pokemon {nombre} ha sido eliminado: ')
    formatear_lista(lista)

#5) Ordenar la lista de pokémons por nombre (alfabéticamente de la Z a la A) 
def ordenar_lista(lista: list):

    formatear_lista(lista)

    for i in range(len(lista) -1) :
        for j in range(i+1, len(lista)):
            if lista[i][0] > lista[j][0]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

    formatear_lista(lista)



#6) Ver héroe más pesado de los de tipo agua (poder ver toda la información de manera amena para el usuario sobre el pokémon más pesado dentro de los de tipo agua) 

def ver_mas(lista: list, tipo: str, indice:int):
    mas_pesado = []

    for i in range(len(lista)):
        print(lista[i][1])
        if lista[i][1] == tipo:
            if mas_pesado == []:
                mas_pesado = lista[i]
                print(mas_pesado)
            elif lista[i][indice] > mas_pesado[indice]:
                mas_pesado = lista[i]
                print(mas_pesado)

    formatear_lista([mas_pesado])
    return mas_pesado

# ver_mas(lista_pokemon, 'Agua', 3)
#7) Ver pokemon con más fuerza de ataque (poder ver toda la información de manera amena para el usuario sobre el pokémon más fuerte) 

def ver_mas_fuerte(lista: list):
    ver_mas(lista, 'Electrico' and 'Fuego' and 'Planta'and 'Agua' and 'Fantasma' and 'Dragon'and \
            'Normal' and 'Psiquico' and 'Lucha'and 'Roca'and 'Siniestro' and 'Acero', 5)
    
#8) Listar sólo los pokemones de una región en particular de una manera amena para el usuario 

def filtrar_por_region(lista: list):
    region = comprobar_region()
    lista_de_la_region = []

    for i in range(len(lista)):
        if lista[i][6] == region:
            lista_de_la_region.append(lista[i])

    formatear_lista(lista_de_la_region)