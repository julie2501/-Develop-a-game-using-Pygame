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
