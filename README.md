# -Develop-a-game-using-Pygame

Here's a simple game using Pygame that involves moving a square around the screen with the arrow keys:

python code
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

x = 200
y = 200
size = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (x, y, size, size))
    pygame.display.update()

    clock.tick(60)
This code first initializes Pygame and creates a window with dimensions of 400x400 pixels. It then sets up a game loop that runs until the user quits the game. Within the loop, it checks for events, including the "QUIT" event that occurs when the user closes the window. It also checks for key presses using the pygame.key.get_pressed() function and updates the position of the square accordingly. Finally, it fills the screen with white, draws the square with blue, updates the display, and sets the game to run at 60 frames per second using the clock.tick(60) function. This game has a total of 15 lines of code.
