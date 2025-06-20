"""Mao ying gomez uribe 
yang li gomez uribe 
yeison andres villegas pabon"""

import pygame 
import sys
import constantes
import math
import time
import random

from model.personaje import Personaje
from model.mundo import Mundo
from model.semaforo import Semaforo
from model.proyectil import Proyectil
from view.pantallafinal import pantalla_final

from view.usuarios_db import obtener_ranking as obtener_ranking_view

from view.usuarios_db import registrar_usuario, login_usuario
from model.puntajes_db import guardar_puntaje, obtener_ranking as obtener_ranking_model
from model.puntajes_db import guardar_puntaje


def cargar_sonido_verde():
    return pygame.mixer.Sound(r'musica\juageremod.mp3')

def cargar_sonido_rojo():
    return pygame.mixer.Sound(r'musica\espalda.mp3')  # Cambia el nombre al que estés usando



#inicializar pygame
pygame.init()


def Main_con_puntaje(user_id):


    ventana = pygame.display.set_mode((constantes.WIDTH, constantes.HEIGHT))


    
    pygame.display.set_caption('LUZ VERDE LUZ ROJA')
    pygame.mixer.init()
    pygame.mixer.music.load(r'musica\juageremod.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    sonido_verde = cargar_sonido_verde()
    sonido_rojo = cargar_sonido_rojo()

    reloj = pygame.time.Clock()
    mundo = Mundo(constantes.WIDTH, constantes.HEIGHT)
    personaje = Personaje(constantes.WIDTH // 50, constantes.HEIGHT // 2)
    semaforo = Semaforo()
    estado_semaforo_anterior = None

    META_X = 990
    tiempo_limite = 40
    tiempo_inicio = pygame.time.get_ticks()

    proyectiles = []
    ultimo_disparo = 0
    intervalo_disparo = 1.0

    zona_segura = pygame.Rect(0, 0, 100, constantes.HEIGHT)
    salio_zona_segura = False
    tiempo_inicio = None




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        semaforo.actualizar()

        if semaforo.estado != estado_semaforo_anterior:
            if semaforo.estado == "LUZ VERDE":
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play(-1)
                sonido_rojo.stop()
            else:
                pygame.mixer.music.stop()
                sonido_rojo.play(-1)

        estado_semaforo_anterior = semaforo.estado

        if not salio_zona_segura and not zona_segura.collidepoint(personaje.x, personaje.y):
            salio_zona_segura = True
            tiempo_inicio = pygame.time.get_ticks()

        tiempo_actual = pygame.time.get_ticks() / 1000  # tiempo en segundos
        if semaforo.estado == "LUZ VERDE" and (tiempo_actual - ultimo_disparo) > intervalo_disparo:
            x_muñeca = constantes.WIDTH - constantes.MUÑECA // 2
            y_muñeca = (constantes.HEIGHT - constantes.MUÑECA) // 2 + constantes.MUÑECA // 2

            for _ in range(2):
                angulo = random.uniform(0, 2 * math.pi)
                dx = math.cos(angulo)
                dy = math.sin(angulo)
                proyectiles.append(Proyectil(x_muñeca, y_muñeca, dx, dy))
            ultimo_disparo = tiempo_actual

        moviendose = keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]

        # Evita eliminar justo en el frame de cambio
        if semaforo.estado == "LUZ ROJA" and moviendose and not semaforo.acaba_de_cambiar():
           
            tiempo_final = 0
            if salio_zona_segura and tiempo_inicio is not None:
                tiempo_final = (pygame.time.get_ticks() - tiempo_inicio) // 1000

            jugar_otra_vez = pantalla_final(ventana, tiempo_final, mensaje="PERDISTE", color_titulo=(234, 67, 53))
            if jugar_otra_vez:
                pygame.time.delay(1000)
                pygame.mixer.stop()
                Main_con_puntaje(user_id)
                pygame.mixer.stop()
            else:
                pygame.quit()
                sys.exit()


        if salio_zona_segura:
            tiempo_actual_ticks = pygame.time.get_ticks()
            teimpo_transcurrido = (tiempo_actual_ticks - tiempo_inicio) // 1000
            tiempo_restante = max(0, tiempo_limite - teimpo_transcurrido)
        else:
            tiempo_restante = tiempo_limite

        if salio_zona_segura and tiempo_restante <= 0:
            pygame.time.delay(1000)
            pantalla_final(ventana, tiempo_final, mensaje="PERDISTE", color_titulo=(234, 67, 53))
            Main_con_puntaje(user_id)
            return

        if keys[pygame.K_LEFT]:
            personaje.Movimientos(-5, 0, mundo)
        if keys[pygame.K_RIGHT]:
            personaje.Movimientos(5, 0, mundo)
        if keys[pygame.K_UP]:
            personaje.Movimientos(0, -5, mundo)
        if keys[pygame.K_DOWN]:
            personaje.Movimientos(0, 5, mundo)

        # --- GUARDAR PUNTAJE AL GANAR ---
        if personaje.x + constantes.PERSONAJE >= META_X:
            pygame.time.delay(1500)
            if salio_zona_segura and tiempo_inicio is not None:
                tiempo_total = (pygame.time.get_ticks() - tiempo_inicio) // 1000
            else:
                tiempo_total = 0
            pantalla_final(ventana, tiempo_total, mensaje="GANASTE", color_titulo=(58, 134, 255))
            Main_con_puntaje(user_id)
            return

        mundo.Dibujar_mundo(ventana)
        personaje.Dibujar_personaje(ventana, semaforo)
        semaforo.dibujar(ventana)

        for proyectil in proyectiles:
            proyectil.dibujar(ventana)
            proyectil.mover()


        # --- SOLO DEJA LA DE DISTANCIA ---
        jugador_centro_x = personaje.x + constantes.PERSONAJE // 2
        jugador_centro_y = personaje.y + constantes.PERSONAJE // 2
        jugador_radio = int(constantes.PERSONAJE * 0.4)  # Ajusta este valor si es necesario

        for proyectil in proyectiles:
            distancia = math.hypot(proyectil.x - jugador_centro_x, proyectil.y - jugador_centro_y)
            if distancia < proyectil.radio + jugador_radio:
                pygame.time.wait(1000)

                jugar_otra_vez = pantalla_final(ventana, tiempo_limite - tiempo_restante)
                if jugar_otra_vez:
                    Main_con_puntaje(user_id)
                    pygame.mixer.stop()
                else:
                    pygame.quit()
                    sys.exit()

                return

        proyectiles = [p for p in proyectiles if 0 <= p.x <= constantes.WIDTH and 0 <= p.y <= constantes.HEIGHT]

        fuente = pygame.font.SysFont(None, 36)
        texto_tiempo = fuente.render(f'{tiempo_restante} segundos', True, (255, 255, 255))
        ventana.blit(texto_tiempo, (100, 20))

        pygame.display.flip()
        reloj.tick(60)










