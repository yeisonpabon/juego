import pygame
import sys
import constantes
from usuarios_db import obtener_ranking

def game_over(ventana, tiempo_total):
    fuente_grande = pygame.font.SysFont(None, 72)
    fuente_pequeña = pygame.font.SysFont(None, 36)

    btn_reiniciar = pygame.Rect(constantes.WIDTH // 2 - 100, constantes.HEIGHT // 2 + 40, 260, 50)

    ranking = obtener_ranking()  # Obtener ranking una sola vez

    while True:
        ventana.fill((245, 245, 220))  # Limpiar la pantalla
        txt_perdiste = fuente_grande.render('GAME OVER', True, (255, 0, 0))
        txt_tiempo = fuente_pequeña.render(f'Tiempo total: {tiempo_total} segundos', True, (0, 0, 0))
        txt_btn = fuente_pequeña.render('JUGAR OTRA VEZ', True, (0, 0, 0))
        # mostrar el texto en la pantalla
        ventana.blit(txt_perdiste, (constantes.WIDTH // 2 - 150, constantes.HEIGHT // 2 - 50))
        ventana.blit(txt_tiempo, (constantes.WIDTH // 2 - 150, constantes.HEIGHT // 2 + 10))
        # dibujar el boton
        pygame.draw.rect(ventana, (255, 255, 0), btn_reiniciar)
        ventana.blit(txt_btn, (btn_reiniciar.x + 25, btn_reiniciar.y + 10))

        # Mostrar el ranking
        y_ranking = btn_reiniciar.y + 70
        txt_ranking = fuente_pequeña.render("Ranking:", True, (0, 0, 0))
        ventana.blit(txt_ranking, (constantes.WIDTH // 2 - 150, y_ranking))
        for i, (username, puntaje) in enumerate(ranking, 1):
            texto = f"{i}. {username} - {puntaje} pts"
            txt_usuario = fuente_pequeña.render(texto, True, (0, 0, 0))
            ventana.blit(txt_usuario, (constantes.WIDTH // 2 - 150, y_ranking + 30 * i))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_reiniciar.collidepoint(event.pos):
                    return  # Reiniciar el juego