import pygame
import random
import time

# 初始化
pygame.init()
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇游戏")
clock = pygame.time.Clock()

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 蛇和食物
snake_block = 20
snake_speed = 15

def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_block, snake_block])

def message(msg, color):
    font = pygame.font.SysFont("simsun", 50)
    text = font.render(msg, True, color)
    screen.blit(text, [width/6, height/3])

def game_loop():
    game_over = False
    game_close = False
    
    # 初始位置
    x1 = width / 2
    y1 = height / 2
    
    # 位置变化
    x1_change = 0
    y1_change = 0
    
    # 蛇身
    snake_list = []
    length_of_snake = 1
    
    # 食物位置
    foodx = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
    
    while not game_over:
        
        while game_close:
            screen.fill(BLACK)
            message("游戏结束! 按Q退出或C重新开始", RED)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0
        
        # 检查是否撞墙
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
            
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        
        # 绘制食物
        pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block])
        
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > length_of_snake:
            del snake_list[0]
            
        # 检查是否撞到自己
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
                
        draw_snake(snake_block, snake_list)
        
        # 显示分数
        font = pygame.font.SysFont("simsun", 35)
        value = font.render(f"分数: {length_of_snake - 1}", True, WHITE)
        screen.blit(value, [0, 0])
        
        pygame.display.update()
        
        # 检查是否吃到食物
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
            length_of_snake += 1
            
        clock.tick(snake_speed)
        
    pygame.quit()
    quit()

game_loop()