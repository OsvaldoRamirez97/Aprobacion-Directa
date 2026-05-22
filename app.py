# 1) Importar la lista de heroes del archivo heroes.py 
from heroes import lista_heroes, lista_de_referencias

'''
Enunciado/s: 
    Industrias Stark decidió ampliar su departamento de IT y creó un desafío de programación para seleccionar candidatos. 
    La empresa compartió información confidencial de distintos superhéroes pertenecientes a diferentes compañías. 
    Cada héroe posee datos como nombre, identidad, altura, peso, género, color de ojos, color de pelo, fuerza e inteligencia. 
    El objetivo será analizar y procesar esta información utilizando estructuras de datos y algoritmos en Python. 
    Nos pidieron hacer una aplicación con un menú que contenga las siguientes opciones: 
    
    Consignas 
        1) Importar la lista de heroes del archivo heroes.py 
        2) Listas todos los héroes de una manera amena para el usuario 
        3) Agregar héroe a la lista (se le pedirá todas las características de un héroe al usuario y se agregará a la lista original:  
            ● nombre e identidad no pueden ser strings vacíos 
            ● la empresa debe ser “DC Comics” o “Marvel Comics” 
            ● peso, altura y fuerza deben ser mayores a 0 
            ● genero M, F, NB 
            ● inteligencia debe ser: “low”, “average”, “good”, “high”, “genius”. 
        4) Eliminar héroe por nombre (el usuario ingresa un nombre y lo intenta eliminar de la lista) 
        5) Ordenar la lista de héroes por nombre (alfabéticamente de la A a la Z) 
        6) Ver héroe más alto (poder ver toda la información de manera amena para el usuario sobre el héroe más alto) 
        7) Ver héroe más fuerte (poder ver toda la información de manera amena para el usuario sobre el héroe más fuerte) 
        8) Ver héroe más delgado; menos pesado (poder ver toda la información de manera amena para el usuario sobre el héroe menos pesado) Objetivos de Aprobación Directa (Calificación de 6 a 10 puntos): 
            ● Integración de todos los temas vistos en clase hasta el momento del parcial, sin usar librerías ni recursos externos 
            ● Que todas las opciones funcionen de manera correcta y el código esté escrito siguiendo todas las buenas prácticas de la programación vistas en clase. 
            ● Poder defender con lenguaje fluido y técnico el entregable 
'''

#2) Listas todos los héroes de una manera amena para el usuario 
#Armar las funciones que reciban las referencias me parecio mas util y legible que escribir cada una de las referencias
def formatear_lista(lista: list, referencias: list = None):
    if referencias is None:
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                print(f'Indice {j}: {lista[i][j]}')
            print('\n')
    else:
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                print(f'{referencias[j]}: {lista[i][j]}')
            print('\n')

#3) Agregar héroe a la lista (se le pedirá todas las características de un héroe al usuario y se agregará a la lista original:  
def agregar_nueva_lista(lista: list, referencias: list = None) -> list:
    nueva_lista = []
    if referencias is None:
        for i in range(len(lista[0])):
            nueva_lista.append(input(f'Ingrese dato {i}: '))
    else:
        for i in range(len(referencias)):
            if referencias[i] == 'Nombre' or referencias[i] == 'Identidad':
                dato = input(f'{referencias[i]}: ')
                while dato == '':
                    dato = input(f'Reingrese {referencias[i].lower()}: ')
                nueva_lista.append(dato)

            elif referencias[i] == 'Empresa':
                dato = input(f'{referencias[i]}: ')
                while dato != 'DC Comics' and dato != 'Marvel Comics' :
                    dato = input(f'Reingrese {referencias[i].lower()}: ')
                nueva_lista.append(dato)

            elif referencias[i] == 'Peso' or referencias[i] == 'Altura' or referencias[i] == 'Fuerza':
                dato = int(input(f'{referencias[i]}: '))
                while dato <= 0:
                    dato = int(input(f'Reingrese {referencias[i].lower()}: '))
                nueva_lista.append(dato)

            elif referencias[i] == 'Genero':
                dato = input(f'{referencias[i]}: ')
                while dato != 'M' and dato != 'F' and dato != 'NB':
                    dato = input(f'Reingrese {referencias[i].lower()}: ')
                nueva_lista.append(dato)

            elif referencias[i] == 'Inteligencia':
                dato = input(f'{referencias[i]}: ')
                while dato != 'low' and dato != 'average' and dato != 'good' and dato != 'high' and dato != 'genius':
                    dato = input(f'Reingrese {referencias[i].lower()}: ')
                nueva_lista.append(dato)
            else:
                dato = input(f'{referencias[i]}: ')
                nueva_lista.append(dato)
    lista.append(nueva_lista)

    formatear_lista(lista)

agregar_nueva_lista(lista_heroes, lista_de_referencias)

#4) Eliminar héroe por nombre (el usuario ingresa un nombre y lo intenta eliminar de la lista) 
def eliminar_item_de_lista(lista: list, referencias: list = None) :
    formatear_lista(lista, referencias)
    dato = input('Ingrese el dato que desea eliminar: ')
    while dato == '':
        dato = input('Reingrese el dato que desea eliminar: ')
    indice = int(input('Ingrese el indice que desea eliminar: '))
    while indice < 0 or indice > len(lista[0]):
        indice = int(input('Reingrese el indice que desea eliminar: '))
    for i in range(len(lista)):
        if lista[i][indice].lower() == dato.lower():
            lista.pop(i)
            break
        elif lista[len(lista)-1][indice].lower() != dato.lower():
            print(f'No se encontro {dato} en la lista!')
    formatear_lista(lista, referencias)

#5) Ordenar la lista de héroes por nombre (alfabéticamente de la A a la Z) 
def ordenar_lista(lista: list, referencias: list) -> list:
    lista_ordenada = []
    print('Elija que indice quiere ordenar: ')
    formatear_lista(lista, referencias)
    indice = int(input(f'Ingrese un indice valido (0 - {len(lista)-1}): '))
    while indice < 0 or indice > len(lista)-1:
        indice = int(input(f'Reingrese un indice valido (0 - {len(lista)-1}): '))

#------------------------------------------------------------ Se hizo muy tarde, continuar desde aca!!! ------------------------------------------------------------

    # for i in range(len(lista)):
    #     if lista[0][indice] < 