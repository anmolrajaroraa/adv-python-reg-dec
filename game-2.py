import pygame
pygame.init()

counter = 0

def displayScore():
    msg = f"Score : {counter}"
    font = pygame.font.SysFont(None, 25, True, True)
    score = font.render(msg, True, red, None)
    screen.blit(score, (0,0))

screenWidth = 500
screenHeight = 300

# Color - red,green,blue (primary colors) 0-255
red = 255,0,0
green = 0,255,0
blue = 0,0,255
black = 0,0,0
white = 255,255,255
newColor = 131,34,134
x = 0
y = 0
rectWidth = 50
rectHeight = 50
radius = 10
moveX = 0
moveY = 0
moveBarX = 0
barWidth = 150
barHeight = 10
ballX, ballY = screenWidth//2, screenHeight - 20 - radius
barX, barY = screenWidth//2 - barWidth // 2, screenHeight - 20
ballShouldMoveWithBar = True

noOfBricks = 10
bricksList = []
widthAvailableForBricks = screenWidth - (radius * (noOfBricks + 1))
print(widthAvailableForBricks)
brickSize = widthAvailableForBricks / noOfBricks
print(brickSize)
brickHeight = 25

for i in range(4):
    for j in range(noOfBricks):
        bricksList.append(((brickSize + 10) * j, 35 * i))

print(bricksList)

screen = pygame.display.set_mode((screenWidth,screenHeight))

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveBarX = -1
                if ballShouldMoveWithBar:
                    moveX = -1
            elif event.key == pygame.K_RIGHT:
                moveBarX = 1
                if ballShouldMoveWithBar:
                    moveX = 1
            elif event.key == pygame.K_SPACE:
                moveY = -1
                moveX = 1
                ballShouldMoveWithBar = False
            # elif event.key == pygame.K_UP:
            #     moveY = -1
            # elif event.key == pygame.K_DOWN:
            #     moveY = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveBarX = 0
                if ballShouldMoveWithBar:
                    moveX = 0
            elif event.key == pygame.K_RIGHT:
                moveBarX = 0
                if ballShouldMoveWithBar:
                    moveX = 0

    screen.fill(white)

    # place to draw, color, (x,y,rectWidth,rectHeight)
    # pygame.draw.rect(screen, newColor, (x,y,rectWidth,rectHeight))
    barRect = pygame.draw.rect(screen, blue, (barX, barY, barWidth, barHeight))
    ballRect = pygame.Rect((ballX-radius, ballY-radius,radius*2,radius*2))
    # pygame.draw.rect(screen,newColor,(ballX-radius, ballY-radius,radius*2,radius*2))
    ball = pygame.draw.circle(screen, red, (ballX, ballY),radius)
    barX = barX + moveBarX
    ballX = ballX + moveX
    ballY = ballY + moveY

    if barRect.colliderect(ballRect):
        moveY = -1
        

    for i,brick in enumerate(bricksList):
        brickRect = pygame.draw.rect(screen, green, (brick[0] + 10, brick[1] + 10, brickSize, brickHeight))
        if brickRect.colliderect(ballRect):
            moveY = 1
            counter += 1
            del bricksList[i]
            break

    displayScore()

    # x = x + moveX
    # y = y + moveY

    # rectangle conditions
    # if y > screenHeight - rectHeight:
    #     moveY = -1
    # elif x > screenWidth - rectWidth:
    #     moveX = -1
    # elif y < 0:
    #     moveY = 1
    # elif x < 0:
    #     moveX = 1

    # if ballY > screenHeight - radius:
    #     moveY = -1
    if ballX > screenWidth - radius:
        moveX = -1
    elif ballY < radius:
        moveY = 1
    elif ballX < radius:
        moveX = 1

    pygame.display.update()    