import pygame
import os

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player Task 2")

# Инициализация микшера
pygame.mixer.init()

# Путь к папке с музыкой
music_folder = 'C:/Users/baqzh/OneDrive/Рабочий стол/labaratory works/LAB7'


# Список песен
songs = [
    "C:/Users/baqzh/OneDrive/Рабочий стол/labaratory works/LAB7/05 - Ed Sheeran - Perfect.mp3",
    "C:/Users/baqzh/OneDrive/Рабочий стол/labaratory works/LAB7/84c7b6c6c7a09006789b7410a57a0003.mp3",
    "C:/Users/baqzh/OneDrive/Рабочий стол/labaratory works/LAB7/Ed Sheeran - Tides.mp3"
]

# Проверяем существование файлов перед загрузкой
songs = [os.path.join(music_folder, song) for song in songs if os.path.exists(os.path.join(music_folder, song))]

if not songs:
    print("Ошибка: нет доступных песен в указанной папке!")
    pygame.quit()
    exit()

current_song = 0  


background_path = os.path.join(music_folder, r"C:\Users\baqzh\Downloads\Lady-Gaga-Bruno-Mars-Die-With-A-Smile-screenshot-billboard-1548.webp")

if os.path.exists(background_path):
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, (WIDTH, HEIGHT)) 
else:
    print("Ошибка: Файл фона не найден! Используется черный экран.")
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((0, 0, 0))  


def play_music():
    """Проигрывает текущую песню."""
    print("Playing:", songs[current_song])
    pygame.mixer.music.load(songs[current_song])
    pygame.mixer.music.play()

def stop_music():
    """Останавливает музыку."""
    print("Music stopped")
    pygame.mixer.music.stop()

def next_song():
    """Переключает на следующую песню."""
    global current_song
    stop_music()
    current_song = (current_song + 1) % len(songs)
    print("Next song:", songs[current_song])
    play_music()

def prev_song():
    """Переключает на предыдущую песню."""
    global current_song
    stop_music()
    current_song = (current_song - 1) % len(songs)
    print("Previous song:", songs[current_song])
    play_music()


play_music()

running = True
while running:
    screen.blit(background, (0, 0)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  
            print(f"Key pressed: {event.key}")
            if event.key == pygame.K_w:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_d:
                next_song()
            elif event.key == pygame.K_a:
                prev_song()
        elif event.type == pygame.KEYUP:
            print(f"Key released: {event.key}")

    pygame.display.flip()

pygame.quit()