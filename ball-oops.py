import pygame
import random
pygame.init()

white = 255, 255, 255
green = 0, 255, 0
red = 255, 0, 0
blue = 0, 0, 255

width = 800
height = 400


class Ball:
    balls_list = []

    def __init__(self):  # initialize the newly created object
        self.x = 0
        self.y = 0
        self.moveX = random.randint(1, 10)
        self.moveY = random.randint(1, 10)
        self.color = random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)
        self.radius = random.randint(10, 50)

    def updateBall(self):
        self.x = self.x + self.moveX
        self.y = self.y + self.moveY
        if self.y > height - self.radius:
            self.moveY = random.randint(-10, -1)
        elif self.x > width - self.radius:
            self.moveX = random.randint(-10, -1)
        elif self.x < self.radius:
            self.moveX = random.randint(1, 10)
        elif self.y < self.radius:
            self.moveY = random.randint(1, 10)


screen = pygame.display.set_mode((width, height))

ball1 = Ball()
ball2 = Ball()
ball3 = Ball()
ball4 = Ball()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)

    pygame.draw.circle(screen, ball1.color, (ball1.x, ball1.y), ball1.radius)
    ball1.updateBall()

    pygame.draw.circle(screen, ball2.color, (ball2.x, ball2.y), ball2.radius)
    ball2.updateBall()

    pygame.draw.circle(screen, ball3.color, (ball3.x, ball3.y), ball3.radius)
    ball3.updateBall()

    pygame.display.update()
