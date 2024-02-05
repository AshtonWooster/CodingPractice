import os
import pygame
pygame.init()

WHITE = (255, 25, 255)

WIDTH, HEIGHT = 1200,800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

smile_ball = pygame.image.load(os.path.join("Assets", "Ball.jpg"))
smile_ball = pygame.transform.scale(smile_ball, (400,400))

def draw_ball(x, y):
    screen.blit(smile_ball, (x,y))

run = True
ball_x, ball_y = 100,100
speed = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # speed = 3
        # pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[pygame.K_a]:
        #     ball_x = ball_x - speed
        # if pressed_keys[pygame.K_d]:
        #     ball_x = ball_x + speed
        # if pressed_keys[pygame.K_w]:
        #     ball_y = ball_y - speed
        # if pressed_keys[pygame.K_s]:
        #     ball_y = ball_y + speed
        
        speed = 20
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                ball_x = ball_x - speed
            if event.key == pygame.K_d:
                ball_x = ball_x + speed
            if event.key == pygame.K_w:
                ball_y = ball_y - speed
            if event.key == pygame.K_s:
                ball_y = ball_y + speed


        screen.fill(WHITE)
        draw_ball(ball_x, ball_y)
        
        pygame.display.update()
        clock.tick(30)

pygame.quit()
