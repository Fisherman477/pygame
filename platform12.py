#----------Initalization and Constants
import pygame
from pygame.locals import *
import random
from random import randint

pygame.init()
vec = pygame.math.Vector2 #Vector2 for 2 dimensions
#vec will help later with realistic movement

#---constant variables 
#variables for initalization and later movement use
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60

#using a clock is more accurate fps controlling
FramePerSecond = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

#----------player initalization and movement
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30,30))
        self.surf.fill((40, 200, 180))
        self.rect = self.surf.get_rect()
        
        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False

    def move(self):
        self.acc = vec(0,0.5)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]: self.acc.x = -ACC
        if pressed_keys[K_RIGHT]: self.acc.x = ACC

        #physics 
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH: self.pos.x = 0
        if self.pos.x < 0: self.pos.x = WIDTH 

        self.rect.midbottom = self.pos

    def update(self):
        hits = pygame.sprite.spritecollide(P1, platforms, False)
        if P1.vel.y > 0:
            if hits:
                if self.pos.y < hits[0].rect.bottom:
                    self.pos.y = hits[0].rect.top + 1
                    self.vel.y = 0
                    self.jumping = False

    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -12
    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -1:
                self.vel.y = -1

#------------FALSE platforms----------------
class Fake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50,100), 12))
        self.surf.fill((200,100,100))
        self.rect = self.surf.get_rect(center = (random.randint(0, WIDTH-10), random.randint(0, HEIGHT-30)))


#------------REAL platforms-----------------
class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50,100), 12))
        self.surf.fill((100,200,100))
        self.rect = self.surf.get_rect(center = (random.randint(0, WIDTH-10), random.randint(0, HEIGHT-30)))


PT1 = Platform()
PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((100,200,100))
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT-10))

P1 = Player()

#-------------------Groups-----------------------------
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

fakes = pygame.sprite.Group()

platforms = pygame.sprite.Group()
platforms.add(PT1)

def plat_gen():
    while len(platforms) < 8:
        width = random.randrange(50,100)
        p = Platform()
        p.rect.center = (random.randrange(0, WIDTH - (width/.5)), random.randrange(-50, 0))
        platforms.add(p)
        all_sprites.add(p)
    while len(fakes) < 6:
        width = random.randrange(50, 100)
        f = Fake()
        f.rect.center = random.randrange(0, WIDTH - (width/.5)), random.randrange(-50, 0)
        fakes.add(f)



def check(platform, groupies):
    if pygame.sprite.spritecollideany(platform, groupies): 
        return True
    else:
        for entity in groupies:
            if entity == platform: 
                continue
            if (abs(platform.rect.top - entity.rect.bottom)) < 20 and (abs(platform.rect.bottom - entity.rect.top))< 20:
                return True
#-------------initial platform generation-------------
#generatres the platforms that appear at the start of the game
def make():
    for x in range(6):
        plat = Platform()
        platforms.add(plat)
        all_sprites.add(plat)
    for x in range(4):
        plant = Fake()
        fakes.add(plant)
make()
#-------------------------main game loop-------------------------------
running = True
while running:
    for event in pygame.event.get(): 
        if event.type == QUIT: running = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP: P1.jump()
            if event.key == pygame.K_r:
                for plat in platforms: 
                    plat.kill()
                for plant in fakes: 
                    plant.kill()
                PT1 = Platform()
                PT1.surf = pygame.Surface((WIDTH, 20))
                PT1.surf.fill((100,200,100))
                PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT-10))
                platforms.add(PT1)
                all_sprites.add(PT1)
                make()
                P1.__init__()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    P1.cancel_jump()

    if P1.rect.top <= HEIGHT/3: #checks the player position
        P1.pos.y += abs(P1.vel.y) #updates the player position as screen moves
        for plat in platforms: 
            plat.rect.y += abs(P1.vel.y) #updates platform positions as screen moves
            if plat.rect.top >= HEIGHT: plat.kill() #kills the platforms when they move below the screen
        for plant in fakes:
            plant.rect.y += abs(P1.vel.y)
            if plant.rect.top >= HEIGHT: plant.kill()

    P1.update()
    P1.move()
    plat_gen()

    #filling the display surface with a solid background color
    displaysurface.fill((0,0,0))

    #loops through all the sprites drawing them on the screen
    for entity in fakes:
        displaysurface.blit(entity.surf, entity.rect)
    for entity in all_sprites: 
        displaysurface.blit(entity.surf, entity.rect)
    

    #updates the display
    pygame.display.update()
    FramePerSecond.tick(FPS)

#quit the gameplay wehen the code exits the main game loop
pygame.quit()
