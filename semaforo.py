

import pygame
import random

class Semaforo:
    def __init__(self):
        self.estado = "LUZ VERDE"
        self.ultimo_cambio = pygame.time.get_ticks() # este metodo obtiene el tiempo actual en milisegundos
        self.duracion = random.randint(3000, 5000)  # de 3 a 5 segundos

    def actualizar(self):
        ahora = pygame.time.get_ticks()
        if ahora - self.ultimo_cambio > self.duracion:
            self.estado = "LUZ ROJA" if self.estado == "LUZ VERDE" else "LUZ VERDE"
            self.ultimo_cambio = ahora
            self.duracion = random.randint(3000, 5000)  # nuevo tiempo aleatorio para el siguiente cambio

    def dibujar(self, pantalla):
        color = (0, 255, 0) if self.estado == "LUZ VERDE" else (255, 0, 0)
        pygame.draw.circle(pantalla, color, (500, 50), 30)  # centro arriba

         
