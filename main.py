import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame in Dev Container")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Ball settings
ball_x = width // 2
ball_y = height // 2
ball_radius = 50
ball_speed_x = 5
ball_speed_y = 5

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce off the walls
    if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius < 0 or ball_y + ball_radius > height:
        ball_speed_y = -ball_speed_y

    # Fill the background
    screen.fill(WHITE)

    # Draw a blue circle
    pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
