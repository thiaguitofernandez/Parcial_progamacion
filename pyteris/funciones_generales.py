import pygame
from constantes import *
import colores
import json

fondo = pygame.image.load(r"imagenes\fondo\cielo-estrellado.jpg")

def chequeo_eventos(jugador,juego,pantalla,grilla):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        juego.terminar_juego()
                match(juego.pantalla_actual):
                        case "pantalla menu principal":
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        posicion_M = pygame.mouse.get_pos()
                                if event.type == pygame.KEYDOWN:

                                        if event.key == pygame.K_BACKSPACE:
                                                juego.jugador_actual = juego.jugador_actual[:-1]
                                        else:
                                                if len(juego.jugador_actual) <= 2:
                                                        juego.jugador_actual += event.unicode
                                        if len(juego.jugador_actual) == 3:
                                                if event.key == pygame.K_RETURN:
                                                        juego.pantalla_actual = "jugando"
                                                        jugador.dibujar_forma(pantalla)
                        case "jugando":
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_DOWN:
                                                jugador.bajar()
                                        elif event.key == pygame.K_LEFT:
                                                jugador.izquierda()
                                        elif event.key == pygame.K_RIGHT:
                                                jugador.derecha()
                                        elif event.key == pygame.K_UP:
                                                jugador.girar()
                                                jugador.decidir_orientacion()
                                                jugador.dibujar_forma(pantalla)
                        case "pantalla game over":
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        posicion_M = pygame.mouse.get_pos()
                                        if juego.boton_reinicio.collidepoint(posicion_M):
                                                grilla.reiniciar()
                                                juego.puntuacion = 0
                                                juego.reiniciar_jugador()
                                                juego.pantalla_actual =  "jugando"
                                                
                                                
                                        elif juego.boton_menu_principal.collidepoint(posicion_M):
                                                grilla.reiniciar()
                                                juego.puntuacion = 0
                                                juego.reiniciar_jugador()                                                
                                                juego.pantalla_actual = "pantalla menu principal"

                                        elif juego.boton_puntuaciones.collidepoint(posicion_M):
                                                grilla.reiniciar()
                                                juego.puntuacion = 0
                                                juego.reiniciar_jugador()         
                                                juego.pantalla_actual = "pantalla puntuaciones"

                        case "pantalla puntuaciones":
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        posicion_M = pygame.mouse.get_pos()
                                        
                                        if juego.boton_menu_principal.collidepoint(posicion_M):
                                                grilla.reiniciar()
                                                juego.puntuacion = 0
                                                juego.reiniciar_jugador()
                                                juego.pantalla_actual = "pantalla menu principal"
        

def chequeo_fondo(Grilla,Jugador):
        for bloque in Jugador.lista_rect:
                x = 75
                for puntos in range(10):
                    x += 30
                    if pygame.Rect.collidepoint(bloque,x,685):
                        Grilla.pasar_a_cuadricula(Jugador)

                        return True


def mostrar_pantalla_inicial(pantalla,fuente_t,fuente_n,juego):
        titulo_txt = fuente_t.render(TITULO,0,colores.WHITESMOKE)
        prompt_nombre_txt = fuente_n.render(PROMPT_NOMBRE,0,colores.WHITESMOKE)
        nombre_jugador_txt = fuente_n.render(juego.jugador_actual,0,colores.WHITESMOKE)
        
        pygame.Surface.blit(pantalla,fondo,(0,0))
        pygame.Surface.blit(pantalla,titulo_txt,(ANCHO_VENTANA * 0.4 ,ALTO_VENTANA * 0.20 ) )
        pygame.Surface.blit(pantalla,prompt_nombre_txt,(ANCHO_VENTANA * 0.3 ,ALTO_VENTANA * 0.45 ) )
        pygame.Surface.blit(pantalla,nombre_jugador_txt,(ANCHO_VENTANA * 0.4 ,ALTO_VENTANA * 0.5 ) )

def mostrar_pantalla_niveles(pantalla,fuente_t,fuente_n,juego):
        puntuacion_txt = fuente_n.render("PUNTUACION : " +str(juego.puntuacion),0,colores.WHITESMOKE)

        pygame.Surface.blit(pantalla,fondo,(0,0))
        pygame.Surface.blit(pantalla,puntuacion_txt,(ANCHO_VENTANA * 0.65 ,ALTO_VENTANA * 0.15 ) )

def mostrar_pantalla_game_over(pantalla,fuente_t,juego):
        


        pygame.Surface.blit(pantalla,fondo,(0,0))
        
        game_over_txt = fuente_t.render(GAME_OVER,0,colores.WHITESMOKE)
        pygame.Surface.blit(pantalla,game_over_txt,(ANCHO_VENTANA * 0.4 ,ALTO_VENTANA * 0.2 ) )

        menu_principal_txt = fuente_t.render(MENU_PRINCIPAL,0,colores.BLACK)
        menu_principal_rect = menu_principal_txt.get_rect()
        menu_principal_rect.move_ip(ANCHO_VENTANA * 0.33 ,ALTO_VENTANA * 0.9 )
        boton_menu_principal = pygame.draw.rect(pantalla,colores.WHITESMOKE,(menu_principal_rect[0] - 25 ,menu_principal_rect[1] - 10 ,menu_principal_rect[2] + 50 ,menu_principal_rect[3] + 20 ))
        pygame.Surface.blit(pantalla,menu_principal_txt,(ANCHO_VENTANA * 0.33 ,ALTO_VENTANA * 0.9 ) )

        reiniciar_txt = fuente_t.render(REINICIAR,0,colores.BLACK)
        reiniciar_rect = reiniciar_txt.get_rect()
        reiniciar_rect.move_ip(ANCHO_VENTANA * 0.33 ,ALTO_VENTANA * 0.75 )
        boton_reiniciar = pygame.draw.rect(pantalla,colores.WHITESMOKE,(reiniciar_rect[0] - 25 ,reiniciar_rect[1] - 10 ,reiniciar_rect[2] + 50 ,reiniciar_rect[3] + 20 ))
        pygame.Surface.blit(pantalla,reiniciar_txt,(ANCHO_VENTANA * 0.33 ,ALTO_VENTANA * 0.75  ) )

        puntuaciones_txt = fuente_t.render(PUNTUACIONES,0,colores.BLACK)
        puntuaciones_rect = puntuaciones_txt.get_rect()
        puntuaciones_rect.move_ip(ANCHO_VENTANA * 0.33 ,ALTO_VENTANA * 0.6 )
        boton_puntuaciones = pygame.draw.rect(pantalla,colores.WHITESMOKE,(puntuaciones_rect[0] - 25 ,puntuaciones_rect[1] - 10 ,puntuaciones_rect[2] + 50 ,puntuaciones_rect[3] + 20 ))
        pygame.Surface.blit(pantalla,puntuaciones_txt,(ANCHO_VENTANA * 0.33 ,ALTO_VENTANA * 0.6 ) )

        juego.botones_game_over(boton_reiniciar,boton_menu_principal,boton_puntuaciones)
        
def mostrar_pantalla_puntuaciones(pantalla,fuente_t,fuente_n,juego,puntuaciones):


        pygame.Surface.blit(pantalla,fondo,(0,0))

        puntuaciones_txt = fuente_t.render(PUNTUACIONES,0,colores.WHITESMOKE)
        pygame.Surface.blit(pantalla,puntuaciones_txt,(ANCHO_VENTANA * 0.30 ,100) )
        titulo_txt = fuente_n.render(TITULO_PUNTUACIONES,0,colores.WHITESMOKE)
        pygame.Surface.blit(pantalla,titulo_txt,(ANCHO_VENTANA * 0.27 ,180) )
        y = 200
        for i in range(10):
                y += 30
                if i >= len(puntuaciones):
                        texto = str(i) + " .                    000"
                else:
                        texto = str(i)+ ". " + puntuaciones[i]["jugador"] + "                    " + str(puntuaciones[i]["puntuacion"])
                puntuacion_txt = fuente_n.render(texto,0,colores.WHITESMOKE)
                pygame.Surface.blit(pantalla,puntuacion_txt,(ANCHO_VENTANA * 0.35 ,y) )

        menu_principal_txt = fuente_t.render(MENU_PRINCIPAL,0,colores.BLACK)
        menu_principal_rect = menu_principal_txt.get_rect()
        menu_principal_rect.move_ip(ANCHO_VENTANA * 0.33 ,ALTO_VENTANA * 0.9 )
        boton_menu_principal = pygame.draw.rect(pantalla,colores.WHITESMOKE,(menu_principal_rect[0] - 25 ,menu_principal_rect[1] - 10 ,menu_principal_rect[2] + 50 ,menu_principal_rect[3] + 20 ))
        pygame.Surface.blit(pantalla,menu_principal_txt,(ANCHO_VENTANA * 0.33 ,ALTO_VENTANA * 0.9 ) )
        juego.botones_puntuaciones(boton_menu_principal)
        
        
def cargar_puntuaciones():
        with open("puntuaciones.json") as archivo:
                puntuaciones = json.load(archivo)
                puntuaciones = puntuaciones["puntajes"]
        for puntaje in puntuaciones:
                puntaje["puntuacion"] = int(puntaje["puntuacion"])
        return puntuaciones
        

        
def ordenar_lista(puntuaciones:list):  
        puntuaciones.sort(reverse = True, key = devoler_diccionario)
        return puntuaciones

def devoler_diccionario(e:dict):
        return e["puntuacion"]










