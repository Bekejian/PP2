import pygame
import sys
import random
import time
import psycopg2

# --------- 数据库连接配置 ---------
conn = psycopg2.connect(
    database="Snake_game",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# --------- 初始化 pygame ---------
pygame.init()

# --------- 用户名输入 ---------
username = input("请输入你的用户名：")

# 查询或创建用户
cur.execute("SELECT id FROM users WHERE username = %s", (username,))
user = cur.fetchone()

if user:
    user_id = user[0]
    print(f"欢迎回来，{username}！")
else:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    print(f"欢迎新玩家，{username}！")

# 查询该用户上次保存的最高记录
cur.execute(
    "SELECT score, level FROM user_scores WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1",
    (user_id,)
)
last_record = cur.fetchone()
score = last_record[0] if last_record else 0
FPS = last_record[1] if last_record else 10

# --------- 游戏设置 ---------
HEIGHT = 600
WIDTH = 600
grid_SIZE = 20
grid_WIDTH = WIDTH // grid_SIZE
grid_HEIGHT = HEIGHT // grid_SIZE
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size()).convert()

# ✅ 中文字体（SimHei）
myfont = pygame.font.SysFont("SimHei", 20)

# --------- 背景网格 ---------
def drawGrid(surface):
    for y in range(0, grid_HEIGHT):
        for x in range(0, grid_WIDTH):
            r = pygame.Rect((x * grid_SIZE, y * grid_SIZE), (grid_SIZE, grid_SIZE))
            color = (93, 216, 228) if (x + y) % 2 == 0 else (84, 194, 205)
            pygame.draw.rect(surface, color, r)

# --------- 蛇 ---------
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 24, 47)
        self.dead = False

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
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

        if new[0] < 0 or new[0] >= WIDTH or new[1] < 0 or new[1] >= HEIGHT:
            self.dead = True
            return

        if new in self.positions[2:]:
            self.dead = True
            return

        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()

    def reset(self):
        self.__init__()

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (grid_SIZE, grid_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

# --------- 食物 ---------
class Food:
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
        r = pygame.Rect(self.position, (grid_SIZE, grid_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

# --------- 游戏开始 ---------
snake = Snake()
food = Food()
death_count = 0  # ✅ 添加死亡次数统计

# --------- 主循环 ---------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            cur.close()
            conn.close()
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
        death_count += 1
        surface.fill((255, 0, 0))
        screen.blit(surface, (0, 0))
        screen.blit(myfont.render("游戏结束！", True, (0, 0, 0)), (WIDTH // 2 - 60, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)

        if death_count == 2:
            # ✅ 第二次死亡后保存并退出
            cur.execute(
                "INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)",
                (user_id, score, FPS)
            )
            conn.commit()
            print(f"🎮 自动保存成功：{username}, 分数={score}, 等级={FPS}")
            pygame.quit()
            cur.close()
            conn.close()
            sys.exit()

        # ✅ 第一次死亡只重启游戏
        snake.reset()
        food.randomize_position()
        score = 0
        FPS = 10
        continue

    drawGrid(surface)
    snake.move()

    if snake.get_head_position() == food.position:
        snake.length += food.weight
        score += food.weight
        FPS += 1
        food.randomize_position()

    if food.is_expired():
        food.randomize_position()

    snake.draw(surface)
    food.draw(surface)
    screen.blit(surface, (0, 0))

    screen.blit(myfont.render(f"用户: {username}", True, (0, 0, 0)), (5, 10))
    screen.blit(myfont.render(f"得分: {score}", True, (0, 0, 0)), (5, 30))
    screen.blit(myfont.render(f"等级: {FPS}", True, (0, 0, 0)), (5, 50))
    screen.blit(myfont.render("自动保存（第2次死亡后）", True, (0, 0, 0)), (5, 70))

    pygame.display.flip()
    clock.tick(FPS)
