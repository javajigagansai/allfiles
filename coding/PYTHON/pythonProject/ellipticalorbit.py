import pygame
import math
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Elliptical Orbits")
black = (0, 0, 0)
white = (255, 255, 255)
def draw_ellipse(a, b, angle, center):
    points = []
    for i in range(360):
        theta = math.radians(i)
        x = a * math.cos(theta)
        y = b * math.sin(theta)
        rotated_x = (x * math.cos(angle)) - (y * math.sin(angle)) + center[0]
        rotated_y = (x * math.sin(angle)) + (y * math.cos(angle)) + center[1]
        points.append((rotated_x, rotated_y))
    pygame.draw.polygon(screen, white, points, 1)
def main():
    clock = pygame.time.Clock()
    angle = 0
    a = 200
    b = 100
    center = (width // 2, height // 2)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(black)
        draw_ellipse(a, b, angle, center)
        angle += 0.01
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__": main()