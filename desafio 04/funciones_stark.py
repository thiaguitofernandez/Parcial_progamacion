import re
from data_stark import *


def extraer_iniciales(nombre_heroe:str):
    iniciales = ""
    if nombre_heroe != "" and nombre_heroe != " ":
        l_iniciales = re.findall("([A-Z])",nombre_heroe)
        for letra in l_iniciales:
            iniciales += letra + "."

    return iniciales

def obtener_dato_formato(dato:str):
    if type(dato) == str :
        dato = re.sub(" ", "_",dato)
        dato.lower()
        retorno = dato
    else:
        retorno = False

    return retorno

def stark_imprimir_nombre_con_iniciales(nombre_heroe:str):
    if type(nombre_heroe) == str:
        
        nombre_formateado = obtener_dato_formato(nombre_heroe)
        iniciales = extraer_iniciales(nombre_heroe)
        mensaje = "*" + nombre_formateado +"("+iniciales +")"
        return mensaje

def stark_imprimir_nombres_con_iniciales(lista):
    if type(lista) == list:
        if len(lista) != 0:
            for heroe in lista:
                print(stark_imprimir_nombre_con_iniciales(heroe["nombre"]))
            retorno = True

        else:retorno = False
    else: retorno = False

    return retorno



def generar_codigo_heroe(heroe,id):
    if heroe["genero"] == "F":
        codigo = "F-2"
    elif heroe["genero"] == "M":
        codigo = "M-1"
    elif heroe["genero"] == "NB":
        codigo = "NB-0"
    else:
        codigo = "N/A"
        if codigo != "N/A":
            id = str(id)
            id.zfill(7)
            codigo += id
    
    return codigo

def stark_generar_codigo_heroe(lista):
    if type(lista) == list:
        if len(lista) != 0:
            for posicion in range(len(lista)):
                if type(lista[posicion]) == dict:
                    nombre = stark_imprimir_nombre_con_iniciales(lista[posicion]["nombre"])
                    codigo = generar_codigo_heroe(lista[posicion],posicion)
                    print(nombre + "|" + codigo)
                else: retorno = False
            retorno = True
        else: retorno = False
    else: retorno = False

    return retorno

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

def sanitizar_string(valor_str:str,valor_por_defecto = "-"):
        numero_str = re.sub("/"," ", numero_str)
        if valor_str.isspace():
            Retorno = valor_por_defecto
        else:
            if valor_str.isnumeric():
                retorno = "N/A"
            else: retorno = valor_str

def sanitizar_dato(heroe:dict,clave:str,tipo_dato:int|float|str):
    retorno = True
    if tipo_dato == int:
        sanitizar_entero(heroe[clave])
    elif tipo_dato == float:
        sanitizar_entero(heroe[clave])
    elif tipo_dato == str:
        sanitizar_entero(heroe[clave])
    else:retorno = False

    return retorno


def stark_normalizar_datos(lista:list):
    if type(lista) == list:
        if len(lista) != 0:
            for heroe in lista:
                sanitizar_dato(heroe,"altura",float)
                sanitizar_dato(heroe,"peso",float)
                sanitizar_dato(heroe,"color_ojos",str)
                sanitizar_dato(heroe,"color_pelo",str)
                sanitizar_dato(heroe,"fuerza",int)
                sanitizar_dato(heroe,"inteligencia",int)
                mensaje = "Datos normalizados"
        else: mensaje = "ERROR: Lista de heroes vacia"
    else: mensaje = "ERROR: No se recibio una lista"
    print(mensaje)
    
def stark_imprimir_inidice_nombre(lista:list):
    mensaje = ""
    for heroe in lista:
        nombre = re.sub("the","",heroe["nombre"])
        nombre = re.sub(" ","-",nombre)
        mensaje += nombre+"-"
    return mensaje

def  generar_separador(patron:str,largo:int,imprimir = True):
    if (len(patron) <= 2 and len(patron) > 0) and (largo <= 235 and largo >= 1):
        mensaje = ""
        
        for duracion in range(largo):
            mensaje += patron 
        
        if imprimir:
            print(mensaje)
        retorno = mensaje
    else: retorno = "N/A"
    return retorno

def generar_encabezado(titulo:str):
    titulo.upper()
    generar_separador("*",20)
    print(titulo)
    generar_separador("*",20)

def imprimir_ficha_heroe(heroe:dict):
    iniciales = extraer_iniciales(heroe)     
    id = lista_personajes.index(heroe)
    mensaje_principal = "     NOMBRE DEL HEROE:       {0[nombre]}({1})\
        \n      IDENTIDAD SECRETA:       {0[identidad]}\
        \n      CONSULTORA:       {0[empresa]}\
        \n      CODIGO DE HEROE:       {2}".format(heroe,iniciales,id)
    
    mensaje_fisico = "      ALTURA:       {0[altura]}cm.\
        \n      PESO:      {0[peso]:.2f}Kg.\
        \n      FUERZA:       {0[fuerza]}N".format(heroe)
    mensaje_particulares = "        COLOR DE OJOS:       {0[color_ojos]}\
        \n      COLOR DE PELO:       {0[colo_pelo]}".format(heroe)

    generar_encabezado("principal")
    print(mensaje_principal)
    generar_encabezado("fisico")
    print(mensaje_fisico)
    generar_encabezado("señas particulares")
    print(mensaje_particulares)

def stark_navega_fichas(lista:list):
    imprimir_ficha_heroe(lista[0])
    puntero_lista = 0
    menu_activo = True
    while menu_activo:
        indicacion = int(input("[1]ir a la izquierda    [2]ir a la derecha      [3]salir"))
        while indicacion == (1 or 2 or 3):
            indicacion = int(input("ERROR: opcion invalidad por favor selecione una opcion valida.\
                                \n[1]ir a la izquierda    [2]ir a la derecha      [3]salir"))
        match(indicacion):
            case 1:
                puntero_lista -= 1
            case 2:
                puntero_lista += 1
            case 3:
                menu_activo = False
        imprimir_ficha_heroe([lista[puntero_lista]])

def stark_menu_pincipal(estado:str,lista:list):
        opcion = input("Ingrese la opcion que desea realizar(0 para mostrar opciones): ")
        if opcion.isnumeric():
            opcion = int(opcion)
            if opcion <= 6 and opcion >= 1:
                return opcion
            else: return False
        else: return False

def imprimir_menu():
    mensaje_menu_principal = "1-Mostrar los nombres con inciales.\
    \n2-Mostrar heroes cpon codigo propio.\
    \n3-Normalizar los datos.\
    \n4-Mostrar indice de nombres.\
    \n5-Navegar atravez de las fichas.\
    \n6-Salir."

    print(mensaje_menu_principal)