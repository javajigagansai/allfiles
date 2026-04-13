import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")

black = (0, 0, 0)
white = (255, 255, 255)
ball_pos = [width // 2, height // 2]
ball_vel = [3, 3]
ball_radius = 20


def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update ball position
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        # Check for collisions with the screen boundaries
        if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > width:
            ball_vel[0] = -ball_vel[0]
        if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > height:
            ball_vel[1] = -ball_vel[1]

        # Fill screen and draw ball
        screen.fill(black)
        pygame.draw.circle(screen, white, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
