import re
from data_stark import lista_personajes
from funciones_stark import *


def stark_marvel_app(lista_personajes:list):
    datos_normalizados = False
    imprimir_menu()
    while True:
            opcion = stark_menu_pincipal("principal",lista_personajes)
            
            match(opcion):
                case 0:
                    imprimir_menu()
                    
                case 1:
                    stark_imprimir_nombres_con_iniciales(lista_personajes)
                case 2:
                    stark_generar_codigo_heroe(lista_personajes)
                case 3:
                    datos_normalizados = True
                    stark_normalizar_datos(lista_personajes)
                case False:
                    print("Error opcion ingresada no coincide con ninguna opcion disponible")
                case 6:
                        break

            if datos_normalizados:
                match(opcion):
                    case 4:
                        stark_generar_codigo_heroe(lista_personajes)
                        
                    case 5:
                        imprimir_ficha_heroe(lista_personajes)

            elif opcion == 4 or opcion == 5:
                print("ERROR: datos no normalizados por favor normalize los datos para aceder a las siguientes opciones.")
                    


stark_marvel_app(lista_personajes)
