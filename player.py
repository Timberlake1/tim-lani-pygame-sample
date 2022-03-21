import pygame
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self,twin,x,y,obstacles):
        super().__init__()
        # Load all animations of character
        self.twin = twin
        self.walk_up = pygame.image.load(f'assets/graphics/{self.twin}/{self.twin}_up.png').convert_alpha()
        self.walk_up = pygame.transform.scale2x(self.walk_up)
        self.walk_down = pygame.image.load(f'assets/graphics/{self.twin}/{self.twin}_down.png').convert_alpha()
        self.walk_down = pygame.transform.scale2x(self.walk_down)
        self.walk_right = pygame.image.load(f'assets/graphics/{self.twin}/{self.twin}_right.png').convert_alpha()
        self.walk_right = pygame.transform.scale2x(self.walk_right)
        self.walk_left = pygame.image.load(f'assets/graphics/{self.twin}/{self.twin}_left.png').convert_alpha()
        self.walk_left = pygame.transform.scale2x(self.walk_left)
        self.image = self.walk_up

        # Variables for smooth movement
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
        self.vx = 0
        self.vy = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4

        # Obstacles
        self.obstacles = obstacles

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.left_pressed = True
        else:
            self.left_pressed = False
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.right_pressed = True
        else:
            self.right_pressed = False
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.up_pressed = True
        else:
            self.up_pressed = False
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.down_pressed = True
        else:
            self.down_pressed = False

    def animation_state(self):
        if self.left_pressed and not self.right_pressed:
            self.image = self.walk_left
        if self.right_pressed and not self.left_pressed:
            self.image = self.walk_right
        if self.up_pressed and not self.down_pressed:
            self.image = self.walk_up
        if self.down_pressed and not self.up_pressed:
            self.image = self.walk_down

    def movement(self):
        self.vx = 0
        self.vy = 0
        if self.left_pressed and not self.right_pressed:
            self.vx = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.vx = self.speed
        if self.up_pressed and not self.down_pressed:
            self.vy = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.vy = self.speed

        # Collision (incomplete)
        if pygame.sprite.spritecollide(self,self.obstacles,False):
            pass

        # Barrier (not a good implementation of barrier, not precise because has some approximation)
        if self.twin == "good":
            if self.x >= 400-32: self.x = 400-32
            if self.x <= 0: self.x = 0
        if self.twin == "evil":
            if self.x >= 800-32: self.x = 800-32
            if self.x <= 400: self.x = 400
        if self.y <= 0: self.y = 0
        if self.y >= 600-32: self.y = 600-32

        self.rect = pygame.Rect(int(self.x), int(self.y), 16, 16)


    def update(self):
        self.player_input()
        self.animation_state()
        self.movement()
