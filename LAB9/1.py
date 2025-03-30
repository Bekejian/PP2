import pygame
import random
import sys

# 初始化Pygame
pygame.init()

# 设置屏幕大小
HEIGHT = 600
WIDTH = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# 加载图片资源
road = pygame.image.load(r"C:\Users\Bakobe\Downloads\AnimatedStreet.png")
coin_i = pygame.image.load(r"C:\Users\Bakobe\Downloads\Coin.png")
coin_im = pygame.transform.scale(coin_i, (100, 100))
player_im = pygame.image.load(r"C:\Users\Bakobe\Downloads\Player.png")
enemy_im = pygame.image.load(r"C:\Users\Bakobe\Downloads\Enemy.png")

# 加载音乐与音效
pygame.mixer.music.load(r"C:\Users\Bakobe\Downloads\background.wav")
pygame.mixer.music.play(-1)
coin_sound = pygame.mixer.Sound(r"C:\Users\Bakobe\Downloads\coin.mp3")
crash_sound = pygame.mixer.Sound(r"C:\Users\Bakobe\Downloads\crash.wav")

# 初始化字体和分数
font = pygame.font.SysFont("Verdana", 30)
score = 0               # 总得分（根据金币权重加分）
coins_collected = 0     # 玩家拾取的金币总数（不论权重）

# 每收集 N 个金币，敌人速度 +1
COINS_FOR_SPEEDUP = 5


# 玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_im
        self.speed = 5
        self.rect = self.image.get_rect()
        self.rect.midbottom = (WIDTH // 2, HEIGHT - 10)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -self.speed)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, self.speed)

        # 防止出界
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


# 金币类
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_im
        self.speed = 7
        self.rect = self.image.get_rect()
        self.weight = random.randint(1, 3)  # 金币的随机权重
        self.generate()

    def generate(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.width)
        self.rect.bottom = 0
        self.weight = random.randint(1, 3)  # 生成新金币时赋予新权重

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate()


# 敌人类
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_im
        self.speed = 8
        self.rect = self.image.get_rect()
        self.generate()

    def generate(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.width)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate()


# 初始化对象和精灵组
player = Player()
coin = Coin()
enemy = Enemy()

all_sprites = pygame.sprite.Group(player, coin, enemy)
coin_sprites = pygame.sprite.Group(coin)
enemy_sprites = pygame.sprite.Group(enemy)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player.move()
    coin.move()
    enemy.move()

    # 玩家碰到金币
    if pygame.sprite.spritecollideany(player, coin_sprites):
        coin_sound.play()
        score += coin.weight              # 加上金币的权重作为分数
        coins_collected += 1              # 每次收集金币 +1（不管权重）
        coin.generate()

        # 每收集 N 个金币，敌人加速
        if coins_collected % COINS_FOR_SPEEDUP == 0:
            enemy.speed += 1

    # 玩家碰到敌人：游戏结束
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()
        pygame.time.delay(1000)
        screen.fill((255, 0, 0))
        game_over_text = font.render("Game Over!", True, (0, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    # 绘制游戏画面
    screen.blit(road, (0, 0))
    all_sprites.draw(screen)

    # 显示分数
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # 显示敌人当前速度（可选）
    speed_text = font.render(f"Enemy Speed: {enemy.speed}", True, (0, 0, 0))
    screen.blit(speed_text, (10, 50))

    pygame.display.flip()
    clock.tick(60)
