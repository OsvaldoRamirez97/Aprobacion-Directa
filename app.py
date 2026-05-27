# 1)  Importar la lista de pokemones del archivo heroes.py 
from pokemons import lista_pokemon

#Indices
NOMBRE = 0 
TIPO = 1 
ALTURA = 2 
PESO = 3 
NIVEL = 4 
FUERZA_ATAQUE = 5 
REGION = 6 


#2) Listas todos los pokemones de una manera amena para el usuario 
def formatear_lista(lista: list):
    
    print(f'\nDatos de los pokemones: ')
    for i in range(len(lista)):
        print(f'\n Nombre: {lista[i][NOMBRE]} \n Tipo: {lista[i][TIPO]} \n Altura: {lista[i][ALTURA]} mts \n Peso: {lista[i][PESO]} kg \
            \n Nivel: {lista[i][NIVEL]} \n Fuerza: {lista[i][FUERZA_ATAQUE]} \n Region: {lista[i][REGION]} \n')



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

    nuevo_pokemon = [nombre, tipo, altura, peso, nivel, fuerza_ataque, region]

    lista.append(nuevo_pokemon)

    print(f'\nPokemon agregado: {nuevo_pokemon[NOMBRE]}!')
    formatear_lista(lista)

#4)Eliminar pokémon  por nombre (el usuario ingresa un nombre y lo intenta eliminar de la lista) 

#Buscar pokemon sirve para reducir la cantidad de responsabilidades de la fucion

def buscar_indice(lista: list, campo: int, dato: str) -> int:
    indice = -1

    for i in range(len(lista)):
        if lista[i][campo] == dato:
            indice = i
            break 

    return indice

def eliminar_pokemon(lista: list):
    formatear_lista(lista)
    nombre = comprobar_str('Ingrese el nombre del pokemon que desea eliminar: ')
    indice_a_eliminar = buscar_indice(lista, NOMBRE, nombre)

    while indice_a_eliminar == -1:
        print('No se encontro el pokemon.')
        nombre = comprobar_str('Reingrese el nombre del pokemon que desea eliminar: ')
        indice_a_eliminar = buscar_indice(lista, nombre)

    print(f'El pokemon {lista[indice_a_eliminar][NOMBRE]} ha sido eliminado: ')

    lista.pop(indice_a_eliminar)
    
    formatear_lista(lista)

#5) Ordenar la lista de pokémons por nombre (alfabéticamente de la Z a la A) 
def ordenar_lista(lista: list):

    formatear_lista(lista)

    for i in range(len(lista) -1) :
        for j in range(i+1, len(lista)):
            if lista[i][NOMBRE] < lista[j][NOMBRE]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

    formatear_lista(lista)



#6) Ver héroe más pesado de los de tipo agua (poder ver toda la información de manera amena para el usuario sobre el pokémon más pesado dentro de los de tipo agua) 

def filtrar_tipo(lista: list, tipo: str = '') -> list:
    lista_filtrada = []
    
    if tipo == '':
        lista_filtrada = lista
    else:
        for i in range(len(lista)):
            if lista[i][TIPO] == tipo:
                lista_filtrada.append(lista[i])

    return lista_filtrada

def filtrar_mas_alto(lista: list, indice:int, tipo: str = ''):
    lista_agua = filtrar_tipo(lista, tipo)
    pokemon_mas_pesado = lista_agua[0]

    for i in range(1, len(lista_agua)):
        if lista_agua[i][indice] > pokemon_mas_pesado[indice]:
            pokemon_mas_pesado = lista_agua[i]

    formatear_lista([pokemon_mas_pesado])


#7) Ver pokemon con más fuerza de ataque (poder ver toda la información de manera amena para el usuario sobre el pokémon más fuerte) 

def ver_mas_fuerte(lista: list):
    filtrar_mas_alto(lista, FUERZA_ATAQUE)
    
#8) Listar sólo los pokemones de una región en particular de una manera amena para el usuario 

def filtrar_por_region(lista: list):
    region = comprobar_region()
    lista_de_la_region = []

    for i in range(len(lista)):
        if lista[i][REGION] == region:
            lista_de_la_region.append(lista[i])

    formatear_lista(lista_de_la_region)

def mostrar_menu():
    print('''
            1 - Ver lista: Ver todos los pokemones
            2 - Agregar: Agregar un nuevo pokemon
            3 - Eliminar: Eliminar un pokemon existente
            4 - Ordenar: Ordenar pokémons por nombre(Z a la A) 
            5 - Pesado: Ver pokemon mas pesado tipo Agua
            6 - Fuerte: Ver pokemon mas fuerte
            7 - Region: Ver pokemones de una region especifica
            8 - Salir: Para finalizar menu
        ''')