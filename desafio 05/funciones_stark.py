
import json
import re

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as file:
            contenido = file.read()
        return contenido
    except Exception as exepcion:
        print("Error al leer el archivo: {0}".format(exepcion))
        return False

def guardar_archivo(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, "w+", encoding="utf-8") as file:
            file.write(contenido)
        print("Se creó el archivo: {0}".format(nombre_archivo))
        return True
    except Exception as exepcion:
        print("Error al crear el archivo: {nombre_archivo}\n{0}".format(exepcion))
        return False

def generar_csv(nombre_archivo, lista_superheroes):
    if lista_superheroes:
        contenido_csv = "nombre,identidad,empresa,altura,peso,genero,color_ojos,color_pelo,fuerza,inteligencia\n"
        for heroe in lista_superheroes:
            contenido_csv += ",".join(str(heroe[key]) for key in heroe) + "\n"
        return guardar_archivo(nombre_archivo, contenido_csv)
    else:
        return False

def leer_csv(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as file:
            lineas = file.readlines()
        
        cabecera = lineas[0].strip().split(",")
        lista_superheroes = []
        for linea in lineas[1:]:
            valores = linea.strip().split(",")
            heroe = {cabecera[i]: valores[i] for i in range(len(cabecera))}
            lista_superheroes.append(heroe)

        return lista_superheroes

    except Exception as exepcion:
        print("Error al leer el archivo CSV: {0}".format(exepcion))
        return False

def generar_json(nombre_archivo, lista_superheroes, nombre_lista):
    if lista_superheroes:
        diccionario = {nombre_lista: lista_superheroes}
        contenido_json = json.dumps(diccionario, indent=4)
        return guardar_archivo(nombre_archivo, contenido_json)
    else:
        return False

def leer_json(nombre_archivo, nombre_lista):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as file:
            contenido = file.read()
        diccionario = json.loads(contenido)
        if nombre_lista in diccionario:
            return diccionario[nombre_lista]
        else:
            return False

    except Exception as exepcion:
        print("Error al leer el archivo JSON: {0}".format(exepcion))
        return False
    

def ordenar_heroes_via_clave(lista:list,clave:str):
    orden = input("Como desea ordenar la lista de forma asc(0) o desc(1):")
    while not(orden == "0" or orden == "1"):
        orden = input("ERROR: orden ingresado no reconocido por favo utilize 0 para orden ascendente o 1 para odern descendente")
    if orden == "0":
        lista = ordenar_asc(lista,clave)
    else:
        lista = ordenar_desc(lista,clave)
    return lista


def ordenar_asc(lista:list,clave:str):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i][clave] > lista[j][clave]:
                aux = lista[i][clave]
                lista[i][clave] = lista[j][clave]
                lista[j][clave] = aux
    return lista


def ordenar_desc(lista:list,clave:str):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i][clave] < lista[j][clave]:
                aux = lista[i][clave]
                lista[i][clave] = lista[j][clave]
                lista[j][clave] = aux
    return lista

def sanitizar_entero(numero_str:str):
    numero_str = re.sub(" ","", numero_str)
    retono = -3
    if numero_str.isnumeric():
        numero = int(numero_str)
        if numero < 0:
            retorno = -2
        else: retorno = numero
    else: retorno = -1

    return retorno


def sanitizar_flotante(numero_str:str):
    numero_str = re.sub(" ","", numero_str)
    if numero_str.isnumeric():
        numero = float(numero_str)
        if numero < 0:
            retorno = -2
        else: retorno = numero
    else: retorno = -1

    return retorno



def sanitizar_dato(heroe:dict,clave:str,tipo_dato:int|float|str):
    retorno = True
    if tipo_dato == int:
        sanitizar_entero(heroe[clave])
    elif tipo_dato == float:
        sanitizar_entero(heroe[clave])
    else:retorno = False

    return retorno


def stark_normalizar_datos(lista:list):
    if type(lista) == list:
        if len(lista) != 0:
            for heroe in lista:
                sanitizar_dato(heroe,"altura",float)
                sanitizar_dato(heroe,"peso",float)
                sanitizar_dato(heroe,"fuerza",int)
                sanitizar_dato(heroe,"inteligencia",int)
                mensaje = "Datos normalizados"
        else: mensaje = "ERROR: Lista de heroes vacia"
    else: mensaje = "ERROR: No se recibio una lista"
    print(mensaje)


def stark_menu_pincipal(estado:str,lista:list):
        opcion = input("Ingrese la opcion que desea realizar(0 para mostrar opciones): ")
        if opcion.isnumeric():
            opcion = int(opcion)
            if opcion <= 6 and opcion >= 1:
                return opcion
            else: return False
        else: return False

def imprimir_menu():
    mensaje_menu_principal = "1-Normalizar los datos.\
    \n2-Generar csv.\
    \n3-Ordenar csv por altura ascendente(nota: debe generar la lista otra vez para que se guarde el cambio).\
    \n4-Generar json.\
    \n5-Ordena json po peso descendiente(nota: debe generar la lista otra vez para que se guarde el cambio).\
    \n6-Ordenar la lista por fuerza.\
    \n7-Salir."

    print(mensaje_menu_principal)



