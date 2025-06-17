import pygame
import constantes
from obstaculos import Arboles
import random
import os



class Mundo():
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.arboles = []  # Lista para almacenar los arboles

        ruta_pasto= os.path.join(r'luzverde-luzroja\imagenes\objetos\Grass_Middle.png')
        self.pasto = pygame.image.load(ruta_pasto).convert()
        self.pasto = pygame.transform.scale(self.pasto,size=(constantes.PASTO,constantes.PASTO))

        ruta_tierra = os.path.join(r'luzverde-luzroja\imagenes\objetos\Path_Middle.png')
        self.tierra = pygame.image.load(ruta_tierra)
        self.tierra = pygame.transform.scale(self.tierra,size=(constantes.TIERRA,constantes.TIERRA))
         

         #generar arboles sin superposicion

        intentos_arboles = 0
        while len(self.arboles) < 20 and intentos_arboles < 1000: # Limitar el numero de intentos para evitar un bucle infinito
            # Generar una posición aleatoria para el arbol
            nuevo_arbol = Arboles(random.randint(60, width - 40), random.randint(0, height - 40))
            if not any(nuevo_arbol.Hit_boxA().colliderect(arbol.Hit_boxA()) for arbol in self.arboles):# Verificar que no colisione con otros arboles
                self.arboles.append(nuevo_arbol)
            intentos_arboles += 1
        



    def Dibujar_mundo (self,pantalla):

        for y in range(0,self.height,constantes.PASTO):
            for x in range(0,self.width,constantes.PASTO):
                pantalla.blit(self.pasto,(x,y))

        for y in range (0,self.width,constantes.TIERRA):
            for x in range (0,self.height,constantes.TIERRA):
                pantalla.blit(self.tierra,(0,y))

        for y in range (0,self.width,constantes.TIERRA):
            for x in range (0,self.height,constantes.TIERRA):
                pantalla.blit(self.tierra,(940,y))

        for arbol in self.arboles:
            if arbol.x < self.width - constantes.ARBOL and arbol.y < self.height - constantes.ARBOL: # Verifica que el árbol esté dentro de los límites
                arbol.Dibujar_arbol(pantalla)
