import json

class game():
    def __init__(self) -> None:
        self.pantalla_actual = "pantalla menu principal"
        self.puntuacion = 0
        self.jugador_actual = ""
        self.guardar = True
        self.nuevo_jugador = False




    def comenzo_juego(self)-> None:
        self.corriendo = True
    
    def terminar_juego(self)-> None:
        self.corriendo = False
    
    def actualizar_puntuacion(self,puntuacion)-> None:
        self.puntuacion = puntuacion
    
    def perdio(self)-> None:
        self.pantalla_actual = "pantalla game over"

    def botones_game_over(self,reinicio,menu_principal,puntuaciones):
        self.boton_reinicio = reinicio
        self.boton_menu_principal = menu_principal
        self.boton_puntuaciones = puntuaciones
    
    def botones_puntuaciones(self,menu_principal):
        self.boton_menu_principal = menu_principal

    def guardar_puntuaciones(self,puntajes):
        puntuaciones = {}
        puntuaciones['puntajes'] = puntajes
        with open("puntuaciones.json", 'w') as archivo:
                json.dump(puntuaciones, archivo, indent=4, ensure_ascii=False )
        self.guardar = False
    
    def reiniciar_jugador(self):
        self.nuevo_jugador = True

    
