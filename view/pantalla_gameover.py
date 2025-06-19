import pygame
import sys
import constantes
from view.usuarios_db import obtener_ranking

def draw_rounded_rect(surface, color, rect, radius=16):
    try:
        pygame.draw.rect(surface, color, rect, border_radius=radius)
    except TypeError:
        pygame.draw.rect(surface, color, rect)

def game_over(ventana, tiempo_total):
    pygame.font.init()
    fuente_titulo = pygame.font.SysFont("Segoe UI", 48, bold=True)
    fuente_normal = pygame.font.SysFont("Segoe UI", 28, bold=True)
    fuente_btn = pygame.font.SysFont("Segoe UI", 20, bold=True)
    fuente_ranking = pygame.font.SysFont("Segoe UI", 22, bold=True)

    # Paleta de colores moderna y suave
    BG = (244, 246, 251)
    FRAME = (255, 255, 255)
    BTN = (58, 134, 255)
    BTN_HOVER = (34, 34, 59)
    BTN_TXT = (255, 255, 255)
    TXT = (34, 34, 59)
    ROJO = (234, 67, 53)
    GRIS = (224, 225, 221)

    # Frame central
    frame_rect = pygame.Rect(constantes.WIDTH // 2 - 200, constantes.HEIGHT // 2 - 180, 400, 400)
    btn_reiniciar = pygame.Rect(constantes.WIDTH // 2 - 100, frame_rect.y + 300, 200, 54)

    ranking = obtener_ranking()
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_reiniciar.collidepoint(event.pos):
                    return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ventana.fill(BG)
        draw_rounded_rect(ventana, FRAME, frame_rect, radius=20)

        # Título
        txt_perdiste = fuente_titulo.render('GAME OVER', True, ROJO)
        ventana.blit(txt_perdiste, (frame_rect.centerx - txt_perdiste.get_width() // 2, frame_rect.y + 32))

        # Tiempo total
        txt_tiempo = fuente_normal.render(f'Tiempo total: {tiempo_total} s', True, TXT)
        ventana.blit(txt_tiempo, (frame_rect.centerx - txt_tiempo.get_width() // 2, frame_rect.y + 100))

        # Ranking
        y_ranking = frame_rect.y + 150
        txt_ranking = fuente_normal.render("Ranking:", True, TXT)
        ventana.blit(txt_ranking, (frame_rect.x + 30, y_ranking))
        for i, (username, puntaje) in enumerate(ranking[:5], 1):
            texto = f"{i}. {username} - {puntaje} pts"
            txt_usuario = fuente_ranking.render(texto, True, TXT)
            ventana.blit(txt_usuario, (frame_rect.x + 30, y_ranking + 34 * i))

        # Botón
        mouse = pygame.mouse.get_pos()
        btn_color = BTN_HOVER if btn_reiniciar.collidepoint(mouse) else BTN
        draw_rounded_rect(ventana, btn_color, btn_reiniciar, radius=16)
        txt_btn = fuente_btn.render('JUGAR OTRA VEZ', True, BTN_TXT)
        ventana.blit(txt_btn, (btn_reiniciar.centerx - txt_btn.get_width() // 2, btn_reiniciar.centery - txt_btn.get_height() // 2))

        pygame.display.flip()