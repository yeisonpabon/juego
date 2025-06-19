import pygame
import constantes
import os
from mundo import Mundo
from obstaculos import Arboles
from constantes import *
from semaforo import Semaforo


class Personaje():

    def __init__(self,x,y):
        self.x = x
        self.y = y

        #cargar hoja de animaciones 
        image_path = os.path.join(r'imagenes\personajes\Player.png')
        self.hoja_animaciones  = pygame.image.load(image_path).convert_alpha()

        #propiedade de  la animacion

        self.tamaño_frame =FRAME_ANIMACION
        self.frame_inicial = 0 #inicia en la posicion 0
        self.tiempo_animacion = 0
        self.animacion_delay = ANIMACION_DELAY
        self.estado_actual = QUIETO_ABAJO
        self.moviendose = False #si nuestro personaje se esta moviendo o no 
        self.mirando_izquierda = False #si nuestro personaje esta mirando hacia la derecha 
        self.animaciones = self.Cargar_animacion()

        #muñeca de frente 
     
        muñeca_path = os.path.join(r'imagenes\personajes\muñecafea.png')
        self.imageM =pygame.image.load(muñeca_path)
        self.imageM = pygame.transform.scale(self.imageM,size=(constantes.MUÑECA,constantes.MUÑECA))
        self.tamañoM = self.imageM.get_width()
#mueñeca de espalda
        muñeca_espalda_path = os.path.join(r'imagenes\personajes\muñecadeespaldas.png')
        self.imageME = pygame.image.load(muñeca_espalda_path)
        self.imageME = pygame.transform.scale(self.imageME,size=(constantes.MUÑECA,constantes.MUÑECA))  
        self.tamañoME = self.imageME.get_width()


    def Cargar_animacion (self):
        animaciones = {} #en un diccionario guardamos nuestras animaciones
        for estados in range(6):
            frames = []
            for frames_path in range(CUADROS_BASICOS):
                surface = pygame.Surface(size = (self.tamaño_frame,self.tamaño_frame),flags=pygame.SRCALPHA)
                surface.blit(self.hoja_animaciones, dest=(0,0),
                area= (frames_path * self.tamaño_frame,
                       estados * self.tamaño_frame,
                       self.tamaño_frame,
                       self.tamaño_frame))
                if constantes.PERSONAJE != self.tamaño_frame:
                    surface = pygame.transform.scale(surface,size=(constantes.PERSONAJE,constantes.PERSONAJE))
                frames.append(surface)
            animaciones[estados] = frames
        return animaciones
    
    def actlizar_animacion(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_animacion > self.animacion_delay:
            self.tiempo_animacion = tiempo_actual
            self.frame_inicial = (self.frame_inicial + 1) % 6


    def Dibujar_personaje(self,pantalla,semaforo):
        frame_actual = self.animaciones[self.estado_actual][self.frame_inicial]
        if self.mirando_izquierda:
            frame_actual = pygame.transform.flip(frame_actual,flip_x=True,flip_y=False) #inverttir el frame para que mire hacia la izquierda
        pantalla.blit(frame_actual,(self.x,self.y))

        #dibujar la muñeca
        x_muñeca = constantes.WIDTH - constantes.MUÑECA #coloca la muñeca justo en el borde del mapa 
        y_muñeca = (constantes.HEIGHT - constantes.MUÑECA)//2 #ubica la muñeca en el centro del mapa

        muñeca_actual = self.imageME if semaforo.estado == "LUZ VERDE" else self.imageM
        pantalla.blit(muñeca_actual, (x_muñeca, y_muñeca))

 

    def Hit_box (self): # rango de colisión del personaje 
        return pygame.Rect(self.x + 5, self.y +5, self.tamaño - 10, self.tamaño -10) 
   #crea un rectangulo de colision mas pequeño que el original.
   #se desplaza el rectangulo un poco hacia adentro ,es decir ya no empieza justo en la esquina
   #self.tamaño -10 reduce el tamaño del rectangulo



    def Movimientos(self,dx,dy,mundo):
        self.moviendose = dx != 0 or dy != 0

        if self.moviendose:
            if dy > 0:
                self.estado_actual = CAMINAR_ABAJO
                self.mirando_izquierda = False

            elif dy < 0 :
                self.estado_actual = CAMINAR_ARRIBA
                self.mirando_izquierda= False
            elif dx > 0 :
                self.estado_actual = CAMINAR_DERECHA
                self.mirando_izquierda = False

            elif dx < 0 :
                self.estado_actual = CAMINAR_DERECHA
                self.mirando_izquierda = True
        else :
            if self.estado_actual == CAMINAR_ABAJO:
               self.estado_actual = QUIETO_ABAJO
            elif self.estado_actual == CAMINAR_ARRIBA:
                self.estado_actual  = QUIETO_ARRIBA
            elif self.estado_actual == CAMINAR_DERECHA:
                self.estado_actual =QUIETO_DERECHA
        new_x = self.x+dx
        new_y = self.y+dy

        for arbol in mundo.arboles:
            if self.Verificar_colicion(new_x,new_y,arbol):
                self.moviendose = False
                return
        
        self.x = new_x
        self.y = new_y
        
        self.x = max (0,min(self.x,constantes.WIDTH-constantes.PERSONAJE))
        self.y = max (0,min(self.y,constantes.HEIGHT- constantes.PERSONAJE))
            
    def Verificar_colicion(self,x,y,objeto):

        hit_boxpersonaje = pygame.Rect(x + 5,y+5, constantes.PERSONAJE -10, constantes.PERSONAJE - 10)
        hit_boxobjeto = objeto.Hit_boxA()
        return hit_boxpersonaje.colliderect(hit_boxobjeto)
    
#se crea un rectangulo temporal en la posicion donde el personaje se quiere mover 
#hit_boxobjeto = objeto.Hit_boxA() pide la hitbox del objeto 
#return hit_boxpersonaje.colliderect(hit_boxobjeto) compara si los rectangulos se estan tocando 




       