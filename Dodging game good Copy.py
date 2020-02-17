import pygame
import sys
import os
import random

pygame.font.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont('Calibri', 25, True, False)

# Class for the player(movement and animaiton)
class player(object):
    def __init__(self):
        # 6 images for the player running animation
        self.image1 = pygame.image.load("Cloud 1.gif")
        self.image2 = pygame.image.load("Cloud 2.gif")
        self.image3 = pygame.image.load("Cloud 3.gif")
        self.image4 = pygame.image.load("Cloud 4.gif")
        self.image5 = pygame.image.load("Cloud 5.gif")
        self.image6 = pygame.image.load("Cloud 6.gif")

        # intial position of the character
        self.x = 0
        self.y = 0

    def control(self):
        # Controls for the player movement
        key = pygame.key.get_pressed()
        speed = 20
        if key[pygame.K_DOWN]:
            self.y += 150
        elif key[pygame.K_UP]:
            self.y -= 150
        if key[pygame.K_RIGHT]:
            self.x += speed
        elif key[pygame.K_LEFT]:
            self.x -= speed
        # Setting restrictions around the border
        if self.y > 350:
            self.y = 0  # Change to --> self.y = 300 to have bottom row to top row movement
        if self.y < 0:
            self.y = 300  # Change to --> self.y = 0 to have top row to bottom row movement
        if self.x < -75:
            self.x = -75
        if self.x > 450:
            self.x = 450

    def draw(self, surface):
        # Animation of the 6 images
        if frame % 6 == 0:
            screen.blit(self.image1, (self.x, self.y))
        elif frame % 6 == 1:
            screen.blit(self.image2, (self.x, self.y))
        elif frame % 6 == 2:
            screen.blit(self.image3, (self.x, self.y))
        elif frame % 6 == 3:
            screen.blit(self.image4, (self.x, self.y))
        elif frame % 6 == 4:
            screen.blit(self.image5, (self.x, self.y))
        elif frame % 6 == 5:
            screen.blit(self.image6, (self.x, self.y))

# Class for score
class score(object):
    def __init__(self):
        self.final = 0

    def start(self):
        self.final += 0.1

def checkCollision(obj1, obj2):
    [obj1x, obj1y, obj1w, obj1h] = obj1
    [obj2x, obj2y, obj2w, obj2h] = obj2

    # check bounding box
    if obj1x + obj1w >= obj2x and obj1x <= obj2x + obj2w:
        if obj1y + obj1h >= obj2y and obj1y <= obj2y + obj2h:
            return True

pygame.init()
W, H = 600, 450
clock = pygame.time.Clock()

# Variables used throughout the code
x = 0
frame = 0
hadouken_x_pos_blue = 0
hadouken_x_pos_blue_2 = 0
hadouken_x_pos_blue_3 = 0
timerCount = -1
timerCount2 = -1
page = 1
running = True

# Projectiles, background, and platform images
screen = pygame.display.set_mode((W, H))
Background = pygame.image.load("Background345.png").convert()
Platform = pygame.image.load("Platform.png").convert()
Blue_1 = pygame.image.load("P_B_1.png").convert()
Blue_2 = pygame.image.load("P_B_2.png").convert()
Blue_3 = pygame.image.load("P_B_3.png").convert()
Blue_4 = pygame.image.load("P_B_4.png").convert()
Game_Over = pygame.image.load("Game Over.jpg").convert()
Start_screen = pygame.image.load("start.png").convert()
Projectile_Blue = [Blue_1, Blue_2, Blue_3, Blue_4]

# Instances
player = player()
score = score()

# Code for the starting screen that leads to the main screen code
while page == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quit the screen
            running = False
    screen.blit((Start_screen), (0, 0))
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        page = 2
        running = True

    pygame.display.flip()
    clock.tick(60)

# main game code that leads to the end screen code
while page == 2 and running == True:
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

    # Calling player controls and increasing frame count
    frame += 1
    player.control()

    # Scrolling background and 2 platforms
    rel_x = x % Background.get_rect().width
    screen.blit(Background, (rel_x - Background.get_rect().width, 0))
    if rel_x < W:
        screen.blit(Background, (rel_x, 0))
    x -= 6
    rel_x = x % Platform.get_rect().width
    screen.blit(Platform, (rel_x - Platform.get_rect().width, 290))
    if rel_x < W:
        screen.blit(Platform, (rel_x, 290))
    x -= 6
    rel_x = x % Platform.get_rect().width
    screen.blit(Platform, (rel_x - Platform.get_rect().width, 140))
    if rel_x < W:
        screen.blit(Platform, (rel_x, 140))
    x -= 6
    pygame.display.update()

    # Bottom projectile movement
    if frame % 4 == 0:
        screen.blit((Projectile_Blue[0]), [hadouken_x_pos_blue + 500, 295])
    elif frame % 4 == 1:
        screen.blit((Projectile_Blue[1]), [hadouken_x_pos_blue + 500, 295])
    elif frame % 4 == 2:
        screen.blit((Projectile_Blue[2]), [hadouken_x_pos_blue + 500, 295])
    else:
        screen.blit((Projectile_Blue[3]), [hadouken_x_pos_blue + 500, 295])
    if hadouken_x_pos_blue + 680 < 0:
        hadouken_x_pos_blue = 0
    #Randomized speed, increasing between 10 to 50
    hadouken_x_pos_blue -= random.randint(10, 50)

    # Middle projectile after 10 seconds
    if timerCount == -1:
        timerCount = 10 * 10
    if timerCount != 0:
        timerCount -= 1
    else:
        if frame % 4 == 0:
            screen.blit((Projectile_Blue[0]), [hadouken_x_pos_blue_2 + 500, 180])
        elif frame % 4 == 1:
            screen.blit((Projectile_Blue[1]), [hadouken_x_pos_blue_2 + 500, 180])
        elif frame % 4 == 2:
            screen.blit((Projectile_Blue[2]), [hadouken_x_pos_blue_2 + 500, 180])
        else:
            screen.blit((Projectile_Blue[3]), [hadouken_x_pos_blue_2 + 500, 180])
        if hadouken_x_pos_blue_2 + 680 < 0:
            hadouken_x_pos_blue_2 = 0
        # Randomized speed, increasing between 10 to 50
        hadouken_x_pos_blue_2 -= random.randint(10, 50)

    # Top projectile after 15 seconds
    if timerCount2 == -1:
        timerCount2 = 15 * 10
    if timerCount2 != 0:
        timerCount2 -= 1
    else:
        if frame % 4 == 0:
            screen.blit((Projectile_Blue[0]), [hadouken_x_pos_blue_3 + 500, 50])
        elif frame % 4 == 1:
            screen.blit((Projectile_Blue[1]), [hadouken_x_pos_blue_3 + 500, 50])
        elif frame % 4 == 2:
            screen.blit((Projectile_Blue[2]), [hadouken_x_pos_blue_3 + 500, 50])
        else:
            screen.blit((Projectile_Blue[3]), [hadouken_x_pos_blue_3 + 500, 50])
        if hadouken_x_pos_blue_3 + 800 < 0:
            hadouken_x_pos_blue_3 = 0
        # Randomized speed, increasing between 10 to 50
        hadouken_x_pos_blue_3 -= random.randint(10, 50)

    # Calling character animation and updating screen
    player.draw(screen)
    pygame.display.update()

    # checking collision between object and the player
    death = checkCollision([player.x, player.y, 160, 160], [hadouken_x_pos_blue + 510, 335, 80, 131])
    death2 = checkCollision([player.x, player.y, 160, 160], [hadouken_x_pos_blue_2 + 535, 230, 45, 50])
    death3 = checkCollision([player.x, player.y, 160, 160], [hadouken_x_pos_blue_3 + 550, 50, 60, 122])

    score.start()

    if death == True or death2 == True or death3 == True:
        running = False
    clock.tick(10)

# End screen code
while running == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(Game_Over, [0, 0])
    screen.blit((font.render("Score:" + str(int(score.final)), True, WHITE)), [260, 350])

    pygame.display.flip()
    clock.tick(60)
