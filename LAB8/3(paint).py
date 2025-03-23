import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_RED = (255, 0, 0)
C_BLUE = (0, 0, 255)
C_GREEN = (0, 255, 0)

color = C_RED
radius = 5
clock = pygame.time.Clock()

drawing = False
last_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                color = C_RED
            if event.key == pygame.K_2:
                color = C_GREEN
            if event.key == pygame.K_3:
                color = C_BLUE
            if event.key == pygame.K_0:
                color = C_WHITE
            if event.key == pygame.K_9:
                color = C_BLACK

    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        if last_pos:
            pygame.draw.line(screen, color, last_pos, mouse_pos, radius)
        last_pos = mouse_pos

    pygame.display.update()
    clock.tick(120) 

pygame.quit()