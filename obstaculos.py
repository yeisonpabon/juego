import pygame
import constantes
import os
class Arboles():
    def __init__(self,x,y):
        self.x = x
        self.y = y

        ruta_arbol = os.path.join(r'luzverde-luzroja\imagenes\objetos\Oak_Tree.png')
        self.arbol = pygame.image.load(ruta_arbol).convert_alpha()
        self.arbol = pygame.transform.scale(self.arbol,size=(constantes.ARBOL,constantes.ARBOL))
        self.tamañoA = self.arbol.get_width()

    def Dibujar_arbol(self,ventana):
        ventana.blit(self.arbol,(self.x,self.y))
        
    def Hit_boxA (self):
        return pygame.Rect(self.x +5 , self.y +5, self.tamañoA -10 , self.tamañoA - 10)
   #crea un rectangulo de colision mas pequeño que el original.
   #se desplaza el rectangulo un poco hacia adentro ,es decir ya no empieza justo en la esquina
   #self.tamaño -10 reduce el tamaño del rectangulo

