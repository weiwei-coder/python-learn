import pygame

# 初始化pygame
pygame.init()

# 设置窗口
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("我的第一个游戏")

# 初始化角色位置
player_x = 400
player_y = 300
player_speed = 5

# 初始化字体
font = pygame.font.SysFont("simsun", 36)

# 游戏主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 填充背景色 (RGB)
    screen.fill((0, 0, 0))

    # 绘制矩形 (颜色, (x, y, 宽度, 高度))
    # pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50))

    # 绘制圆形 (颜色, 中心点, 半径)
    # pygame.draw.circle(screen, (0, 255, 0), (400, 300), 30)

    # 绘制线条 (颜色, 起点, 终点, 宽度)
    # pygame.draw.line(screen, (0, 0, 255), (0, 0), (800, 600), 2)

    # 加载和显示图像
    player_img = pygame.image.load('player.png')  # 需要准备图片文件
    screen.blit(player_img, (200, 200))

    # 在游戏循环中添加
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # 绘制角色
    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    pygame.draw.rect(screen, (255, 255, 0), player_rect)

    # 创建障碍物
    obstacle_rect = pygame.Rect(300, 200, 100, 100)

    # 在游戏循环中检测碰撞
    if player_rect.colliderect(obstacle_rect):
        print("碰撞发生了!")
        pygame.draw.rect(screen, (255, 0, 255), obstacle_rect)  # 碰撞时改变颜色
    else:
        pygame.draw.rect(screen, (0, 255, 255), obstacle_rect)

    # 在游戏循环中渲染文本
    score = 0
    score_text = font.render(f"分数: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    # 更新显示
    pygame.display.flip()

# 退出游戏
pygame.quit()