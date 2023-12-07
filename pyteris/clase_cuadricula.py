import colores
import pygame
from constantes import *
from clase_linea_completa import *


class Cuadricula():
    def __init__(self,) -> None:
        lista_celdas = []
        y = 0
        for verticales in range(22):
            y += 30
            x = 90
            for horizontal in range(10):
                celda = {}
                celda["cordenadas"] = (x,y)
                celda["estado"] = 0
                celda["color"] = None
                celda["rect"] = None
                lista_celdas.append(celda)
                x += 30
        self.celdas = lista_celdas
        self.bandera = False

    def dibujar(self,pantalla)-> None:
        x = 90
        y = 0

        while x <= 390:
            pygame.draw.line(pantalla,colores.GRAY,(x,0),(x,690),1)
            x += 30
        while y <= 690:
            pygame.draw.line(pantalla,colores.GRAY,(90,y),(390,y),1)
            y += 30
            
    def pasar_a_cuadricula(self,forma):
        for celda in self.celdas:
            x_celda = celda["cordenadas"][0]
            y_celda = celda["cordenadas"][1]
            for rect in forma.lista_rect:
                x_forma = rect[0]
                y_forma = rect[1]
                if (x_celda == x_forma) and (y_celda == y_forma):
                    celda["color"] = forma.color
                    celda["estado"] = 1

    def dibujar_contenido(self,pantalla)-> None:
        for celda in self.celdas:
            if celda["estado"] == 1:
                x = celda["cordenadas"][0]
                y = celda["cordenadas"][1]
                celda["rect"] = pygame.draw.rect(pantalla,celda["color"],(x,y,TAMAÑO_BLOQUE,TAMAÑO_BLOQUE))
    
    def chequeo_linea_completa(self,juego)-> None:
        contador = 0
        posiciones = []
        y = self.celdas[0]["cordenadas"][1]
        for celda in self.celdas:
            x = celda["cordenadas"][0]
            if y != celda["cordenadas"][1]:
                y = celda["cordenadas"][1]
                contador = 0
            if celda["estado"] == 1:
                contador += 1
            if contador == 10:
                posiciones.append(self.celdas.index(celda))
                contador = 0
                self.bandera = True
            
        for linea in posiciones:
            linea_completa.add(animacion_linea( (self.celdas[linea]["cordenadas"][1] + 15) ))
            for i in range(10):
                self.celdas[linea-i]["estado"] = 0
                self.celdas[linea-i]["color"] = None
                self.celdas[linea-i]["rect"] = None
        suma_puntuacion = 100 * len(posiciones)
        juego.puntuacion += suma_puntuacion
        


    def bajada_tras_linea_linea_completa(self):
        contador = -1
        while self.bandera:
            termino = True
            contador = -1
            for celda in self.celdas:
                contador += 1
                if contador >= 10:
                    celda_arriba = self.celdas.index(celda) - 10
                    if (self.celdas[celda_arriba]["estado"] == 1) and (celda["estado"] == 0):
                        termino = False
                        celda["estado"] = self.celdas[celda_arriba]["estado"]
                        celda["color"] = self.celdas[celda_arriba]["color"]
                        self.celdas[celda_arriba]["estado"] = 0
                        self.celdas[celda_arriba]["color"] = None
                        self.celdas[celda_arriba]["rect"] = None
            if termino:
                self.bandera = False
                return

    def reiniciar(self)-> None:
        self.celdas = None
        lista_celdas = []
        y = 0
        for verticales in range(22):
            y += 30
            x = 90
            for horizontal in range(10):
                celda = {}
                celda["cordenadas"] = (x,y)
                celda["estado"] = 0
                celda["color"] = None
                celda["rect"] = None
                lista_celdas.append(celda)
                x += 30
        self.celdas = lista_celdas