"""Mao ying gomez uribe 
yang li gomez uribe 
yeison andres villegas pabon"""

import pygame 
import sys
import constantes
from personaje import Personaje
from mundo import Mundo
from semaforo import Semaforo
from proyectil import Proyectil
import math
import time
import random
from pantalla_gameover import game_over
#ini cializar pygame
pygame.init()
 # ...código existente...
from usuarios_db import registrar_usuario, login_usuario
from puntajes_db import guardar_puntaje, obtener_ranking


















def menu_inicio():
    while True:
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Ver ranking")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")
            registrar_usuario(usuario, contraseña)
        elif opcion == "2":
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")
            user_id = login_usuario(usuario, contraseña)
            if user_id:
                print("Login exitoso. ¡A jugar!")
                Main_con_puntaje(user_id)
            else:
                print("Usuario o contraseña incorrectos.")
        elif opcion == "3":
            ranking = obtener_ranking()
            print("Ranking:")
            for i, (username, puntaje) in enumerate(ranking, 1):
                print(f"{i}. {username} - {puntaje}")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")
















# ...importaciones existentes...
from puntajes_db import guardar_puntaje

def Main_con_puntaje(user_id):


    
    ventana = pygame.display.set_mode((constantes.WIDTH,constantes.HEIGHT))  

    pygame.display.set_caption('LUZ VERDE LUZ ROJA')
    pygame.mixer.init()
    pygame.mixer.music.load(r'luzverde-luzroja\musica\musicajuego.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    reloj = pygame.time.Clock()
    mundo = Mundo(constantes.WIDTH, constantes.HEIGHT)
    personaje = Personaje(constantes.WIDTH // 50, constantes.HEIGHT // 2)
    semaforo = Semaforo()

    META_X = 990
    tiempo_limite = 10
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
        tiempo_actual = time.time()

        if not salio_zona_segura and not zona_segura.collidepoint(personaje.x, personaje.y):
            salio_zona_segura = True
            tiempo_inicio = pygame.time.get_ticks()

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

        if semaforo.estado == "LUZ ROJA" and moviendose:
            print("¡Te moviste en LUZ ROJA!")
            tiempo_final = 0
            if salio_zona_segura and tiempo_inicio is not None:
                tiempo_final = (pygame.time.get_ticks() - tiempo_inicio) // 1000

            pygame.time.delay(1500)
            game_over(ventana, tiempo_final)
            Main_con_puntaje(user_id)
            return

        if salio_zona_segura:
            tiempo_actual_ticks = pygame.time.get_ticks()
            teimpo_transcurrido = (tiempo_actual_ticks - tiempo_inicio) // 1000
            tiempo_restante = max(0, tiempo_limite - teimpo_transcurrido)
        else:
            tiempo_restante = tiempo_limite

        if salio_zona_segura and tiempo_restante <= 0:
            pygame.time.delay(1500)
            game_over(ventana, tiempo_limite)
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
            print("GANASTE")
            fuente = pygame.font.SysFont(None, 72)
            texto_victoria = fuente.render("¡GANASTE!", True, (255, 255, 0))
            ventana.blit(texto_victoria, (constantes.WIDTH // 2 - 100, constantes.HEIGHT // 2 - 36))
            pygame.display.flip()
            pygame.time.delay(3000)
            guardar_puntaje(user_id, tiempo_restante)  # Guarda el puntaje del usuario
            pygame.quit()
            sys.exit()

        mundo.Dibujar_mundo(ventana)
        personaje.Dibujar_personaje(ventana, semaforo)
        semaforo.dibujar(ventana)

        for proyectil in proyectiles:
            proyectil.dibujar(ventana)
            proyectil.mover()

        rect_jugador = pygame.Rect(personaje.x, personaje.y, constantes.MUÑECA, constantes.MUÑECA)
        for proyectil in proyectiles:
            rect_bala = pygame.Rect(proyectil.x - proyectil.radio, proyectil.y - proyectil.radio, proyectil.radio * 2, proyectil.radio * 2)
            if rect_jugador.colliderect(rect_bala):
                pygame.time.wait(2000)
                Main_con_puntaje(user_id)
                return

        proyectiles = [p for p in proyectiles if 0 <= p.x <= constantes.WIDTH and 0 <= p.y <= constantes.HEIGHT]

        fuente = pygame.font.SysFont(None, 36)
        texto_tiempo = fuente.render(f'{tiempo_restante} segundos', True, (255, 255, 255))
        ventana.blit(texto_tiempo, (100, 20))

        pygame.display.flip()
        reloj.tick(60)



from usuarios_db import obtener_ranking

# ...código del juego...
# yang li no entendio 

# Al final del juego, muestra el ranking:
ranking = obtener_ranking()
print("Ranking:")
for i, (username, puntaje) in enumerate(ranking, 1):
    print(f"{i}. {username} - {puntaje} puntos")

#TENGO HAMBRE, HACEMOS VACA?
#HOLA
#tenemos que comer algo pq estoy partida del hambre
#bueno ya chao 


#EN LA CASA HAY SOPA

#hola y
#mao dice chao


if __name__ == '__main__':
    menu_inicio()

 