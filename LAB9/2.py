import pygame
import sys
import random
import time

# 初始化
pygame.init()

# 游戏设置
HEIGHT = 600
WIDTH = 600
grid_SIZE = 20
grid_WIDTH = WIDTH // grid_SIZE
grid_HEIGHT = HEIGHT // grid_SIZE
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
FPS = 10  # 初始帧率

# 初始化屏幕
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size()).convert()

# 绘制背景网格
def drawGrid(surface):
    for y in range(0, grid_HEIGHT):
        for x in range(0, grid_WIDTH):
            r = pygame.Rect((x * grid_SIZE, y * grid_SIZE), (grid_SIZE, grid_SIZE))
            if (x + y) % 2 == 0:
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                pygame.draw.rect(surface, (84, 194, 205), r)

# 蛇类
class Snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 24, 47)
        self.dead = False

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        # 防止掉头（180°反转）
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        if self.dead:
            return

        cur = self.get_head_position()
        x, y = self.direction
        new = (cur[0] + x * grid_SIZE, cur[1] + y * grid_SIZE)

        # 撞墙就死
        if new[0] < 0 or new[0] >= WIDTH or new[1] < 0 or new[1] >= HEIGHT:
            self.dead = True
            return

        # 撞到自己也死
        if new in self.positions[2:]:
            self.dead = True
            return

        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.dead = False

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (grid_SIZE, grid_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

# 食物类
class Food(object):
    def __init__(self):
        self.color = (223, 163, 49)
        self.position = (0, 0)
        self.weight = 1
        self.spawn_time = 0
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_WIDTH - 1) * grid_SIZE,
                         random.randint(0, grid_HEIGHT - 1) * grid_SIZE)
        self.weight = random.randint(1, 3)
        self.spawn_time = time.time()

    def is_expired(self):
        return time.time() - self.spawn_time > 3

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (grid_SIZE, grid_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

# 初始化
snake = Snake()
food = Food()
score = 0
myfont = pygame.font.SysFont("monospace", 16)

# 游戏主循环
while True:
    # 事件监听：键盘控制方向
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.turn(UP)
            elif event.key == pygame.K_DOWN:
                snake.turn(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.turn(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.turn(RIGHT)

    if snake.dead:
        # 游戏结束界面
        surface.fill((255, 0, 0))
        game_over = myfont.render("Game Over!", True, (0, 0, 0))
        screen.blit(surface, (0, 0))
        screen.blit(game_over, (WIDTH // 2 - 60, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        snake.reset()
        food.randomize_position()
        score = 0
        FPS = 10
        continue

    drawGrid(surface)
    snake.move()

    # 吃到食物
    if snake.get_head_position() == food.position:
        snake.length += food.weight
        score += food.weight
        FPS += 1
        food.randomize_position()

    # 食物超时刷新
    if food.is_expired():
        food.randomize_position()

    # 绘制元素
    snake.draw(surface)
    food.draw(surface)
    screen.blit(surface, (0, 0))

    # 显示分数 & 食物权重
    score_text = myfont.render(f"Score: {score}", 1, (0, 0, 0))
    food_text = myfont.render(f"Food Weight: {food.weight}", 1, (0, 0, 0))
    screen.blit(score_text, (5, 10))
    screen.blit(food_text, (5, 30))

    pygame.display.flip()
    clock.tick(FPS)
