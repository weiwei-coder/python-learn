import pygame
import sys

# 初始化
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2D平台游戏")
clock = pygame.time.Clock()

# 颜色
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# 玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (100, 300)
        self.velocity_y = 0
        self.jumping = False
    
    def update(self):
        # 重力
        self.velocity_y += 0.5
        if self.velocity_y > 10:
            self.velocity_y = 10
        self.rect.y += self.velocity_y
        
        # 检查是否落地
        if self.rect.bottom >= 550:
            self.rect.bottom = 550
            self.velocity_y = 0
            self.jumping = False
        
        # 键盘控制
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_SPACE] and not self.jumping:
            self.velocity_y = -12
            self.jumping = True

# 平台类
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# 创建精灵组
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

# 创建玩家
player = Player()
all_sprites.add(player)

# 创建平台
ground = Platform(0, 550, 800, 50)
all_sprites.add(ground)
platforms.add(ground)

# 添加一些平台
platform_list = [
    (100, 400, 100, 20),
    (300, 300, 100, 20),
    (500, 200, 100, 20)
]

for plat in platform_list:
    p = Platform(*plat)
    all_sprites.add(p)
    platforms.add(p)

# 游戏循环
running = True
while running:
    # 保持循环以正确的速度运行
    clock.tick(60)
    
    # 处理输入事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 更新
    all_sprites.update()
    
    # 检查玩家是否站在平台上
    if player.velocity_y > 0:  # 如果玩家正在下落
        hits = pygame.sprite.spritecollide(player, platforms, False)
        if hits:
            player.rect.bottom = hits[0].rect.top
            player.velocity_y = 0
            player.jumping = False
    
    # 渲染
    screen.fill(BLACK)
    all_sprites.draw(screen)
    
    # 刷新屏幕
    pygame.display.flip()

pygame.quit()
sys.exit()