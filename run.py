# run.py
import pygame
from agent import Agent
from environment import Environment

# Initialize Pygame
pygame.init()

# Set up the environment
WIDTH, HEIGHT = 600, 400
environment = Environment(WIDTH, HEIGHT)

# Create the agent
agent = Agent(x=WIDTH // 2, y=HEIGHT // 2, speed=5, environment=environment)

# Set up the Pygame window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agent-Environment Simulation")

# Set up font for displaying coordinates
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        agent.move("up")
    if keys[pygame.K_DOWN]:
        agent.move("down")
    if keys[pygame.K_LEFT]:
        agent.move("left")
    if keys[pygame.K_RIGHT]:
        agent.move("right")

    # Fill the screen with a background color
    window.fill((30, 30, 30))

    # Draw the agent as a circle
    pygame.draw.circle(window, (255, 100, 100), (agent.x, agent.y), 10)

    # Display the agent's position
    position_text = font.render(f"Position: ({agent.x}, {agent.y})", True, (255, 255, 255))
    window.blit(position_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
