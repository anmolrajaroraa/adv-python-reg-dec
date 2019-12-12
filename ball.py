import pygame
pygame.init()

white = 255,255,255
green = 0,255,0
red = 255,0,0
blue = 0,0,255
x = 0
y = 0
x2 = 0
y2 = 0
x3 = 0
y3 = 0
moveX = 1
moveY = 1
moveX2 = 2
moveY2 = 2
moveX3 = 3
moveY3 = 3
width = 500
height = 300

screen = pygame.display.set_mode((width,height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)

    pygame.draw.circle(screen, red, (x,y), 50)
    pygame.draw.circle(screen, green, (x2,y2), 50)
    pygame.draw.circle(screen, blue, (x3,y3), 50)

    x = x + moveX
    y = y + moveY
    x2 = x2 + moveX2
    y2 = y2 + moveY2
    x3 = x3 + moveX3
    y3 = y3 + moveY3

    if y > height - 50:
        moveY = -1
    elif x > width - 50:
        moveX = -1
    elif x < 50:
        moveX = 1
    elif y < 50:
        moveY = 1

    if y2 > height - 50:
        moveY2 = -2
    elif x2 > width - 50:
        moveX2 = -2
    elif x2 < 50:
        moveX2 = 2
    elif y2 < 50:
        moveY2 = 2

    if y3 > height - 50:
        moveY3 = -3
    elif x3 > width - 50:
        moveX3 = -3
    elif x3 < 50:
        moveX3 = 3
    elif y3 < 50:
        moveY3 = 3

    pygame.display.update()