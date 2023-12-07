
import copy
from data_stark import lista_personajes
from funciones_stark import *



def stark_marvel_app(lista_personajes:list):
    datos_normalizados = False
    imprimir_menu()
    bandera_csv = False
    bandera_json = False
    while True:
            opcion = stark_menu_pincipal("principal",lista_personajes)
            
            match(opcion):
                case 0:
                    imprimir_menu()
                    
                case 1:
                    stark_normalizar_datos(lista_personajes)
                    datos_normalizados = True

                case 7:
                    return

                case False:
                    print("Error opcion ingresada no coincide con ninguna opcion disponible")

                
            if datos_normalizados:

                match(opcion):
                    case 2:
                        if bandera_csv:
                            generar_csv(r"desafio 05\data_stark.csv",lista_csv)
                        else:
                            lista_csv = copy.deepcopy(lista_personajes)
                            bandera_csv = generar_csv(r"desafio 05\data_stark.csv",lista_csv)
                        
                    case 3:
                        if bandera_csv:
                            lista_csv = ordenar_asc(lista_csv,"altura")
                        else:
                            print("Erorr 404: la lista a ordenar no existe por favo cree la lista con la opcion anterior.")
                    case 4:
                        if bandera_json: 
                            bandera_json = generar_json(r"desafio 05\data_stark.json",lista_json,"lista personajes")
                        else:
                            lista_json = copy.deepcopy(lista_personajes)
                            bandera_json = generar_json(r"desafio 05\data_stark.json",lista_json,"lista personajes")
                            
                    case 5:
                        if bandera_json:
                            lista_json = ordenar_desc(lista_json,"peso")
                        else:
                            print("Erorr 404: la lista a ordenar no existe por favo cree la lista con la opcion anterior.")
                    case 6:
                        lista_personajes = ordenar_heroes_via_clave(lista_personajes,"peso")


stark_marvel_app(lista_personajes)
