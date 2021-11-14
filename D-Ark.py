import pygame

pygame.init()
win = pygame.display.set_mode ((500, 500))
pygame.display.set_caption ("D-Ark")

x = 50
y = 50
width = 40
height = 60

x_vel = 0.0
y_vel = 0.0
max_vel = 5.0

run = True

while run:
    pygame.time.delay (100)
    
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x_vel -= .1

    if keys[pygame.K_RIGHT]:
        x_vel += .1

    if keys[pygame.K_UP]:
        y_vel -= .25

    if keys[pygame.K_DOWN]:
        y_vel += .25

    if x_vel > max_vel:
        x_vel = max_vel

    if x_vel < -max_vel:
        x_vel = -max_vel

    if y_vel > max_vel:
        y_vel = max_vel

    if y_vel < -max_vel:
        y_vel = -max_vel

    if (x_vel > -.1) & (x_vel < .1):
        x_vel = 0.0

    if (y_vel > -.1) & (y_vel < .1):
        y_vel = 0.0

    x += x_vel
    y += y_vel

    x_vel *= .9
    y_vel *= .9

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()