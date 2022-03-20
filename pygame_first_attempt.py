import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()
test_red = pygame.Surface((100,200))
test_red.fill('Red')
test_blue = pygame.Surface((100,200))
test_blue.fill('Blue')
test_silver = pygame.Surface((100,50))
test_silver.fill('Silver')
screen = pygame.display.set_mode((800,400))
x = 100
y = 350
a = 500
b = 350
speed = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))
    blue_box = test_blue.get_rect(midbottom = (x,y))
    screen.blit(test_blue,blue_box)
    silver_box = test_silver.get_rect(midbottom = (500,60))
    screen.blit(test_silver,silver_box)

    userInput = pygame.key.get_pressed()
    
    if userInput[pygame.K_LEFT]:
        x -= speed
    if userInput[pygame.K_RIGHT]:
        x += speed
    if blue_box.colliderect(silver_box) == False:
        if userInput[pygame.K_UP]:
            y -= speed
        if userInput[pygame.K_DOWN]:
            y += speed
    
    red_box = test_red.get_rect(midbottom = (a,b))
    screen.blit(test_red,red_box)

    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT]:
        a -= speed
    if userInput[pygame.K_RIGHT]:
        a += speed
    if red_box.colliderect(silver_box) == False:
        if userInput[pygame.K_UP]:
            b -= speed
        if userInput[pygame.K_DOWN]:
            b += speed
    

    red_box.colliderect(silver_box)
    pygame.display.update()
    clock.tick(60)
