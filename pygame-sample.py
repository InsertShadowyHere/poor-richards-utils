import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800), pygame.DOUBLEBUF)
pygame.display.set_caption("I'm a game")


def draw():
    pygame.draw.circle(screen, (100, 255, 100), (80, 80), 50)


# GAME LOOP
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            pass

    draw()

    pygame.display.flip()
pygame.quit()