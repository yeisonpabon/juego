import pygame
import random

class Semaforo:
    def __init__(self):
        self.estado = "LUZ VERDE"
        self.ultimo_cambio = pygame.time.get_ticks() # este metodo obtiene el tiempo actual en milisegundos
        self.duracion = random.randint(3000, 5000)  # de 3 a 5 segundos
        self.cambio_reciente = False

    def actualizar(self):
        ahora = pygame.time.get_ticks()
        self.cambio_reciente = False  # Reinicia el flag cada frame
        if ahora - self.ultimo_cambio > self.duracion:
            self.estado = "LUZ ROJA" if self.estado == "LUZ VERDE" else "LUZ VERDE"
            self.ultimo_cambio = ahora
            self.duracion = random.randint(3000, 5000)  # nuevo tiempo aleatorio para el siguiente cambio
            self.cambio_reciente = True  # Marca que hubo un cambio exacto en este frame

    def acaba_de_cambiar(self):
        return self.cambio_reciente

    def dibujar(self, pantalla):
        color = (0, 255, 0) if self.estado == "LUZ VERDE" else (255, 0, 0)
        centro = (500, 50)
        radio = 30

        # Dibuja el borde negro (más grande)
        pygame.draw.circle(pantalla, (0, 0, 0), centro, radio + 4)

        # Dibuja el círculo del semáforo encima
        pygame.draw.circle(pantalla, color, centro, radio)

