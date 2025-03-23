import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_RED = (255, 0, 0)
C_BLUE = (0, 0, 255)
C_GREEN = (0, 255, 0)

color = C_BLACK
saved_color = color  
radius = 5
clock = pygame.time.Clock()

drawing = False
last_pos = None
shape = "circle"
eraser_mode = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PLUS:
                shape = "circle"
            if event.key == pygame.K_MINUS:
                shape = "rect"
            if event.key == pygame.K_SPACE:
                shape = "line"
            if event.key == pygame.K_1:
                color = C_RED
                saved_color = color
                eraser_mode = False
            if event.key == pygame.K_2:
                color = C_GREEN
                saved_color = color
                eraser_mode = False
            if event.key == pygame.K_3:
                color = C_BLUE
                saved_color = color
                eraser_mode = False
            if event.key == pygame.K_0:
                color = C_WHITE
                saved_color = color
                eraser_mode = False
            if event.key == pygame.K_9:
                color = C_BLACK
                saved_color = color
                eraser_mode = False
            if event.key == pygame.K_e:
                color = C_WHITE
                eraser_mode = True
            if event.key == pygame.K_b:
                color = saved_color
                eraser_mode = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                current_pos = event.pos
                if shape == "circle":
                    center = ((last_pos[0] + current_pos[0]) // 2,
                              (last_pos[1] + current_pos[1]) // 2)
                    radius_circle = max(abs(current_pos[0] - last_pos[0]) // 2,
                                        abs(current_pos[1] - last_pos[1]) // 2)
                    pygame.draw.circle(screen, color, center, radius_circle)

                elif shape == "rect":
                    rect = pygame.Rect(min(last_pos[0], current_pos[0]),
                                       min(last_pos[1], current_pos[1]),
                                       abs(current_pos[0] - last_pos[0]),
                                       abs(current_pos[1] - last_pos[1]))
                    pygame.draw.rect(screen, color, rect)

                elif shape == "line":
                    pygame.draw.line(screen, color, last_pos, current_pos, radius)
            drawing = False
            last_pos = None

    if drawing and shape == "line":
        mouse_pos = pygame.mouse.get_pos()
        if last_pos:
            pygame.draw.line(screen, color, last_pos, mouse_pos, radius)
        last_pos = mouse_pos

    pygame.display.update()
    clock.tick(120)

pygame.quit()