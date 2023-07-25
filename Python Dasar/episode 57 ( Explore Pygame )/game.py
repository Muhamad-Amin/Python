import pygame

pygame.init()
isRun = True
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar, window_panjang))
x = 250
y = 250
panjang = 20
lebar = 20
speed = 10
while isRun:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < window_lebar - lebar:
        x += speed
    if keys[pygame.K_DOWN] and y < window_panjang - panjang:
        y += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 120, 0), (x, y, lebar, panjang))
    pygame.display.update()
pygame.quit()
