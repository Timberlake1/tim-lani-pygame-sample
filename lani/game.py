import pygame
from sys import exit
import player
import obstacle

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

# Background
good_surf = pygame.Surface((400,600))
good_surf.fill((208,247,247))
evil_surf = pygame.Surface((400,600))
evil_surf.fill((228,184,255))

# Obstacles
obstacles = pygame.sprite.Group()
obstacles.add(obstacle.Wall(600,300))

# Player
good = pygame.sprite.GroupSingle()
good.add(player.Player("good",200,300,obstacles))
evil = pygame.sprite.GroupSingle()
evil.add(player.Player("evil",600,300,obstacles))

while True:
    # Check User Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Update Game
    screen.blit(good_surf,(0,0))
    screen.blit(evil_surf,(400,0))
    good.draw(screen)
    good.update()
    evil.draw(screen)
    evil.update()
    obstacles.draw(screen)
    obstacles.update()

    # Render Game
    pygame.display.update()
    clock.tick(60) # Control fps