import pygame
import sys
import time
pygame.init() 

WIDTH, HEIGHT = 900, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")
clock_image = pygame.image.load("C:/Users/baqzh/OneDrive/Рабочий стол/labaratory works/LAB7/clock.png")
clock_image = pygame.transform.scale(clock_image, (WIDTH, HEIGHT))
minute_hand = pygame.image.load("C:/Users/baqzh/OneDrive/Рабочий стол/labaratory works/LAB7/min_hand.png")  
second_hand = pygame.image.load("C:/Users/baqzh/OneDrive/Рабочий стол/labaratory works/LAB7/sec_hand.png")  
minute_hand = pygame.transform.scale(minute_hand, (700, 700))  
second_hand = pygame.transform.scale(second_hand, (650, 650))  

def rotate_hand(image, angle, pivot):
    """Сағат тілдерін айналдыру функциясы."""
    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=pivot)
    return rotated_image, new_rect

running = True
while running:
    screen.blit(clock_image, (0, 0))  # Фонды салу

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    milliseconds = time.time() % 1 
    print(f" ----\n{minutes}\n{seconds}")

    minute_angle = 6 * (minutes + seconds / 60) + 45  
    second_angle = 6 * (seconds + milliseconds) -48 

    # Тілдерді экранға шығару
    rotated_minute_hand, minute_rect = rotate_hand(minute_hand, minute_angle, CENTER)
    screen.blit(rotated_minute_hand, minute_rect.topleft)

    rotated_second_hand, second_rect = rotate_hand(second_hand, second_angle, CENTER)
    screen.blit(rotated_second_hand, second_rect.topleft)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
sys.exit()