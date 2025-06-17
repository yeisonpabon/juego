import pygame

class Proyectil:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx  # Dirección en X
        self.dy = dy  # Dirección en Y
        self.radio = 7
        self.color = (255, 0, 0)
        self.velocidad = 5

    def mover(self):
        self.x += self.dx * self.velocidad
        self.y += self.dy * self.velocidad

    def dibujar(self, ventana):
        pygame.draw.circle(ventana, self.color, (int(self.x), int(self.y)), self.radio)