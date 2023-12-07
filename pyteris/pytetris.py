import pygame
import constantes
from funciones_generales import *
from clase_juego import game
from clase_jugador import eleccion_forma
from clase_jugador import Formas
from clase_cuadricula import *
from variables_varias import *


pygame.init
## config inicial
Juego = game()
Juego.comenzo_juego()
    ## config pantalla
pantalla = pygame.display.set_mode((constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA))
pygame.display.set_caption(constantes.NOMBRE_VETANA)

    ## config sonido
pygame.mixer.init()
musica = pygame.mixer.music.load(r"sonido\musica tetris original.mp3")
pygame.mixer.music.set_volume((0.1))
pygame.mixer.music.play(-1)
    ## config fuentes
pygame.font.init()
fuente = pygame.font.Font(None,30)
titulo = pygame.font.Font(None,50)


##seteo inicial
Jugador = eleccion_forma()

puntuaciones = cargar_puntuaciones()

Grilla = Cuadricula()
tiempo = pygame.time.Clock
while Juego.corriendo:
    match(Juego.pantalla_actual):
        case "pantalla menu principal":
            mostrar_pantalla_inicial(pantalla,titulo,fuente,Juego)
            #colisiones boton
        case "jugando":
            bajada_auto += 1
            if not(Jugador.bajo) and bajada_auto >= 60:
                Jugador.bajar()
                bajada_auto = 0
            elif Jugador.bajo and bajada_auto >= 60:
                Jugador.bajo = False
                bajada_auto = 0

            for celda in Grilla.celdas:
                if celda["rect"] != None:
                    lista_colisiones = celda["rect"].collidelistall(Jugador.lista_rect)
                    if len(lista_colisiones) != 0:
                        for colision in lista_colisiones:
                            Jugador.subir(Juego)
                            Grilla.pasar_a_cuadricula(Jugador)
                            Grilla.chequeo_linea_completa(Juego)
                            Jugador = eleccion_forma()
                            Jugador.dibujar_forma(pantalla)
           
            if chequeo_fondo(Grilla,Jugador):
                Grilla.chequeo_linea_completa(Juego)
                Jugador = eleccion_forma()
                Jugador.dibujar_forma(pantalla)
        
            mostrar_pantalla_niveles(pantalla,titulo,fuente,Juego)
            Jugador.blitear_forma(pantalla)
            Grilla.dibujar_contenido(pantalla)
            linea_completa.update()
            if not(any in linea_completa ):
                Grilla.bajada_tras_linea_linea_completa()
            linea_completa.draw(surface=pantalla)
            Grilla.dibujar(pantalla)
            
        case "pantalla game over":
            mostrar_pantalla_game_over(pantalla,titulo,Juego)
            
            if Juego.guardar:
                puntuaciones.append({"jugador":Juego.jugador_actual,"puntuacion":Juego.puntuacion})
                Juego.guardar_puntuaciones(puntuaciones)
                
        case "pantalla puntuaciones":
            puntuaciones = ordenar_lista(puntuaciones)
            mostrar_pantalla_puntuaciones(pantalla,titulo,fuente,Juego,puntuaciones)
            


    chequeo_eventos(Jugador,Juego,pantalla,Grilla)
    if Juego.nuevo_jugador:
        Jugador = eleccion_forma()
        Jugador.dibujar_forma(pantalla)
        Juego.nuevo_jugador = False
    pygame.display.flip()
    #tiempo
    pygame.time.Clock().tick(60)
pygame.quit