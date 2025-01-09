import pygame
import random

# Vindustørrelse
vindux = 800 #576
vinduy = 600 #324

# Retninger
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9
LEFT = 2
RIGHT = 4
UP = 5
DOWN = 6

# Ildkulefarten 
MOVESPEED = 7

# Initiering av pygame
pygame.init()
overflate = pygame.display.set_mode((vindux, vinduy))
pygame.display.set_caption("Spill test")

# Importerer bakgrunnsbildene
bg1 = pygame.image.load("BG/Clouds1/1.png")
bg2 = pygame.image.load("BG/Clouds1/2.png")
bg3 = pygame.image.load("BG/Clouds1/3.png")
bg4 = pygame.image.load("BG/Clouds1/4.png")

# Tilpasser bakrunnen til vinduet
t_bg1 = pygame.transform.scale(bg1, (vindux, vinduy))
t_bg2 = pygame.transform.scale(bg2, (vindux, vinduy))
t_bg3 = pygame.transform.scale(bg3, (vindux, vinduy))
t_bg4 = pygame.transform.scale(bg4, (vindux, vinduy))



# Representerer ildkulene i spillet
class ild:
    def __init__(self, x, y, width, height, retning):
        self.bilde = pygame.image.load("Ild.png").convert_alpha()
        self.bilde = pygame.transform.scale(self.bilde, (width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.direction = retning
        
    def beveg(self):
        # Flytter ildkulene basert på nåværende retning
        if self.direction == DOWNLEFT:
            self.rect.left -= MOVESPEED
            self.rect.top += MOVESPEED
        elif self.direction == DOWNRIGHT:
            self.rect.left += MOVESPEED
            self.rect.top += MOVESPEED
        elif self.direction == UPLEFT:
            self.rect.left -= MOVESPEED
            self.rect.top -= MOVESPEED
        elif self.direction == UPRIGHT:
            self.rect.left += MOVESPEED
            self.rect.top -= MOVESPEED
        elif self.direction == LEFT:
            self.rect.left += MOVESPEED
        elif self.direction == RIGHT:
            self.rect.left -= MOVESPEED
        elif self.direction == UP:
            self.rect.top -= MOVESPEED
        elif self.direction == DOWN:
            self.rect.top += MOVESPEED
            
    def check_bounds(self, width, height):
        #Sjekker og korrigerer blokkens posisjon når den treffer kantene.
        if self.rect.top < -100:
            # Ildkula har gått over toppen
            if self.direction == UPLEFT:
                self.direction = DOWNLEFT
            elif self.direction == UPRIGHT:
                self.direction = DOWNRIGHT
            elif self.direction == UP:
                self.direction = DOWN
        if self.rect.bottom > vinduy + 100:
            # Ildkula har gått under bunnen
            if self.direction == DOWNLEFT:
                self.direction = UPLEFT
            elif self.direction == DOWNRIGHT:
                self.direction = UPRIGHT
            elif self.direction == DOWN:
                self.direction = UP
        if self.rect.left < -100:
            # Ildkula har gått over venstre siden
            if self.direction == DOWNLEFT:
                self.direction = DOWNRIGHT
            elif self.direction == UPLEFT:
                self.direction = UPRIGHT
            elif self.direction == LEFT:
                self.direction = RIGHT
        if self.rect.right > vindux + 100:
            # Ildkula har gått over høyresiden
            if self.direction == DOWNRIGHT:
                self.direction = DOWNLEFT
            elif self.direction == UPRIGHT:
                self.direction = UPLEFT
            elif self.direction == RIGHT:
                self.direction = LEFT 
        
    def tegn(self, surface):
        overflate.blit(self.bilde, (self.rect.x, self.rect.y))
        
# Opprett ildkulene
ildkuler = [ild(300, 300, 50, 50, UPRIGHT),
            ild(300, 300, 50, 50, UPLEFT),
            ild(300, 300, 50, 50, DOWNLEFT),
            ild(300, 300, 50, 50, DOWNRIGHT),
            ild(300, 300, 50, 50, RIGHT),
            ild(300, 300, 50, 50, LEFT),
            ild(300, 300, 50, 50, UP),
            ild(300, 300, 50, 50, DOWN)]


# Hovedspill løkke
clock = pygame.time.Clock()
run = True
while run:
    # Avslutter spillet hvis slutt hendelse
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            
    # Opptater ildkulene
    for ildkule in ildkuler:
        ildkule.beveg()
        ildkule.check_bounds(vindux, vinduy)

    # Fjerner bakgrunnen        
    overflate.fill((0, 0, 0))
        
    # Tegner bakgrunnene
    overflate.blit(t_bg1, (0, 0))
    overflate.blit(t_bg2, (0, 0))
    overflate.blit(t_bg3, (0, 0))
    overflate.blit(t_bg4, (0, 0))
    
    # Tegner ildkua
    for ildkule in ildkuler:
        ildkule.tegn(overflate)
    
    # Opptaterer skjermen
    pygame.display.update()
    
    # Setter FPS (frames per second)
    clock.tick(60)

# Avslutter pygame
pygame.quit()