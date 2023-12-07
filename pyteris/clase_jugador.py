import colores
import random
from funciones_generales import *

def eleccion_forma():

    probabilidad_bloque = random.randint(0, 100)
    if probabilidad_bloque < 10:
        forma_elegida =  Formas(colores.SKYBLUE,"I")
    elif probabilidad_bloque < 30:
        forma_elegida =  Formas(colores.PURPLE,"T")
    elif probabilidad_bloque < 60:
        probabilidad_lado = random.randint(0, 100) 
        if probabilidad_lado <= 50:
            forma_elegida = Formas(colores.RED1,"Z derecha")
        else: forma_elegida =  Formas(colores.GREEN2,"Z izquierda")
    elif probabilidad_bloque < 70:
        forma_elegida =  Formas(colores.YELLOW2,"cuadrado")
    elif probabilidad_bloque <=100:
        probabilidad_lado = random.randint(0, 100) 
        if probabilidad_lado <= 50:
            forma_elegida = Formas(colores.BLUE,"L derecha")
        else: forma_elegida = Formas(colores.CARROT,"L izquierda")

    return forma_elegida


#formas
class Formas:
    def __init__(self,color,nombre) -> None:
        match(nombre):
            case"cuadrado":
                self.forma =[
                    [1,1],
                    [1,1]
                ]
                self.color = color
                self.image = r"imagenes\formas tetris\cuadrado.png"
                
            case "I":
                self.forma =[
                    [1],
                    [1],
                    [1],
                    [1]
                ]
                self.color = color
                self.image = r"imagenes\formas tetris\I.png"
                
            case "T":
                self.forma =[
                    [0,1,0],
                    [1,1,1]
                ]
                self.color = color
                self.image = r"imagenes\formas tetris\T.png"

            case "Z derecha":
                self.forma =[
                    [1,1,0],
                    [0,1,1]
                ]
                self.color = color
                self.image = r"imagenes\formas tetris\Z_derecha.png"

            case "Z izquierda":
                self.forma =[
                    [0,1,1],
                    [1,1,0]
                ]
                self.color = color
                self.image = r"imagenes\formas tetris\Z_izquierda.png"

            case "L derecha":
                self.forma =[
                    [1,0],
                    [1,0],
                    [1,1]
                ]
                self.color = color
                self.image = r"imagenes\formas tetris\L_derecha.png"
                
            case "L izquierda":
                self.forma =[
                    [0,1],
                    [0,1],
                    [1,1]
                ]
                self.color = color
                self.image = r"imagenes\formas tetris\L_izquierda.png"

        self.orientacion = 1
        self.cor_img = ((COMIENZO_GRILLA_X + 120),(COMIENZO_GRILLA_Y + 0))
        self.nombre = nombre
        self.image = pygame.image.load(self.image)
        self.bajo = False

    def dibujar_forma(self,pantalla,)-> None:
        lista_rect = []
        
        y = self.cor_img[1]-30
        for fila in self.forma:
            y += 30
            x = self.cor_img[0]-30
            for bloque in fila:
                x += 30
                if bloque == 1:
                    rect = pygame.draw.rect(pantalla,self.color,(x,y,TAMAÑO_BLOQUE,TAMAÑO_BLOQUE))
                    lista_rect.append(rect)
        self.lista_rect = lista_rect

    def blitear_forma(self,pantalla):
        pantalla.blit(self.image,self.cor_img)

    def forma_recta(self):
        match(self.nombre):
            case"cuadrado":
                self.forma = [
                    [1,1],
                    [1,1]
                ]                
            case"T":
                self.forma =[
                    [0,1,0],
                    [1,1,1]
                ]
            case"I":
                self.forma =[
                    [1],
                    [1],
                    [1],
                    [1]
                ]
            case"Z derecha":
                self.forma =[
                    [1,1,0],
                    [0,1,1]
                ]
            case"Z izquierda":
                self.forma =[
                    [0,1,1],
                    [1,1,0]
                ]
            case"L derecha":
                self.forma =[
                    [1,0],
                    [1,0],
                    [1,1]
                ]
            case"L izquierda":
                self.forma =[
                    [0,1],
                    [0,1],
                    [1,1]
                ]
    def forma_derecha(self):
        match(self.nombre):
            case"cuadrado":
                self.forma =[
                    [1,1],
                    [1,1]
                ]
            case"T":
                self.forma =[
                    [1,0],
                    [1,1],
                    [1,0]
                ]
            case"I":
                self.forma =[
                    [1,1,1,1]
                ]
            case"Z derecha":
                self.forma =[
                    [0,1],
                    [1,1],
                    [1,0]
                ]
            case"Z izquierda":
                self.forma =[
                    [1,0],
                    [1,1],
                    [0,1]
                ]
            case"L derecha":
                self.forma =[
                    [1,1,1],
                    [1,0,0]
                ]
            case"L izquierda":
                self.forma =[
                    [1,0,0],
                    [1,1,1]
                ]
    def forma_revez(self):
        match(self.nombre):
            case"cuadrado":
                self.forma = [
                    [1,1],
                    [1,1]
                ]
            case"T":
                self.forma =[
                    [1,1,1],
                    [0,1,0]
                ]
            case"I":
                self.forma =[
                    [1],
                    [1],
                    [1],
                    [1]
                ]
            case"Z derecha":
                self.forma =[
                    [1,1,0],
                    [0,1,1]
                ]
            case"Z izquierda":
                self.forma =[
                    [0,1,1],
                    [1,1,0]
                ]
            case"L derecha":
                self.forma =[
                    [1,1],
                    [0,1],
                    [0,1]
                ]
            case"L izquierda":
                self.forma =[
                    [1,1],
                    [1,0],
                    [1,0]
                ]
    def  forma_izquierda(self):
            match(self.nombre):
                case"cuadrado":
                    self.forma = [
                        [1,1],
                        [1,1]
                    ]
                case"T":
                    self.forma =[
                        [0,1],
                        [1,1],
                        [0,1]
                    ]
                case"I":
                    self.forma =[
                        [1,1,1,1]
                    ]
                case"Z derecha":
                    self.forma =[
                        [0,1],
                        [1,1],
                        [1,0]
                    ]
                case"Z izquierda":
                    self.forma =[
                        [1,0],
                        [1,1],
                        [0,1]
                    ]
                case"L derecha":
                    self.forma =[
                        [0,0,1],
                        [1,1,1]
                    ]
                case"L izquierda":
                    self.forma =[
                        [1,1,1],
                        [0,0,1]
                    ]
    def decidir_orientacion(self):
        match(self.orientacion):
            case 1:
                self.forma_recta()
            case 2:
                self.forma_derecha()
            case 3:
                self.forma_revez()
            case 4:
                self.forma_izquierda()

    def subir(self,juego):
        for bloque in self.lista_rect:
            if bloque[1] <= COMIENZO_GRILLA_X + 60:
                juego.perdio()
                return
            
        for bloque in self.lista_rect:
            bloque.move_ip(0,-30)
        self.cor_img = ((self.cor_img[0]),(self.cor_img[1] - 30))
        
    def bajar(self):
        for bloque in self.lista_rect:
            if bloque[1]+30 >= FIN_GRILLA_Y:
                return
            
        for bloque in self.lista_rect:
            bloque.move_ip(0,30)
        self.cor_img = ((self.cor_img[0]),(self.cor_img[1] + 30))
        self.bajo = True

    def derecha(self):
        for bloque in self.lista_rect:
            if bloque[0]+30 >= FIN_GRILLA_X:
                return
            
        for bloque in self.lista_rect:
            bloque.move_ip(30,0)
        self.cor_img = ((self.cor_img[0] + 30),(self.cor_img[1]))

    def izquierda(self):
        for bloque in self.lista_rect:
            if bloque[0]-30 <= COMIENZO_GRILLA_X:
                return
            
        for bloque in self.lista_rect:
            bloque.move_ip(-30,0)
        self.cor_img = ((self.cor_img[0]- 30),(self.cor_img[1] ))


    def girar(self):
        self.orientacion += 1 if self.orientacion < 4 else -3
        self.image = pygame.transform.rotate(self.image, -90)


        