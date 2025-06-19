import pygame
import sys
import constantes

def mostrar_pantalla_inicio(ventana):
    fuente_titulo = pygame.font.SysFont("Segoe UI", 48, bold=True)
    fuente_texto = pygame.font.SysFont("Segoe UI", 24)
    fuente_btn = pygame.font.SysFont("Segoe UI", 28, bold=True)

    fondo = pygame.Surface((constantes.WIDTH, constantes.HEIGHT))
    fondo.fill((34, 34, 59))  # Color oscuro de fondo

    # Simula un desenfoque
    blur = pygame.transform.smoothscale(fondo, (constantes.WIDTH//10, constantes.HEIGHT//10))
    blur = pygame.transform.smoothscale(blur, (constantes.WIDTH, constantes.HEIGHT))

    btn_rect = pygame.Rect(constantes.WIDTH//2 - 100, constantes.HEIGHT - 120, 200, 50)
    clock = pygame.time.Clock()

    esperando = True
    while esperando:
        clock.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and btn_rect.collidepoint(evento.pos):
                esperando = False

        ventana.blit(blur, (0, 0))

        # Instrucciones
        titulo = fuente_titulo.render("LUZ VERDE, LUZ ROJA", True, (255, 255, 255))
        texto1 = fuente_texto.render("Usa las flechas para moverte", True, (230, 230, 230))
        texto2 = fuente_texto.render("¡No te muevas en LUZ ROJA!", True, (230, 230, 230))
        texto3 = fuente_texto.render("Evita los proyectiles. Llega a la meta.", True, (230, 230, 230))

        ventana.blit(titulo, (constantes.WIDTH//2 - titulo.get_width()//2, 80))
        ventana.blit(texto1, (constantes.WIDTH//2 - texto1.get_width()//2, 180))
        ventana.blit(texto2, (constantes.WIDTH//2 - texto2.get_width()//2, 220))
        ventana.blit(texto3, (constantes.WIDTH//2 - texto3.get_width()//2, 260))

        color_btn = (58, 134, 255) if not btn_rect.collidepoint(pygame.mouse.get_pos()) else (34, 34, 59)
        pygame.draw.rect(ventana, color_btn, btn_rect, border_radius=10)

        txt_btn = fuente_btn.render("INICIAR JUEGO", True, (255, 255, 255))
        ventana.blit(txt_btn, (btn_rect.centerx - txt_btn.get_width()//2,
                               btn_rect.centery - txt_btn.get_height()//2))

        pygame.display.flip()