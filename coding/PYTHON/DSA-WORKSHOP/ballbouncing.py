import pygame
import sys
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ball_radius = 20
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_dx = 5  # Change in x (horizontal speed)
ball_dy = 5  # Change in y (vertical speed)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ball_x += ball_dx
    ball_y += ball_dy
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
        ball_dx *= -1  # Reverse direction horizontally
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= screen_height:
        ball_dy *= -1  # Reverse direction vertically
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    clock.tick(60)
