import pygame
import random

# Vindustørrelse
vindux = 800 #576
vinduy = 600 #324

# Ildkulefarten 
MOVESPEED = 7

# Retninger
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9
LEFT = 2
RIGHT = 4
UP = 5
DOWN = 6
RETNINGER = [UPLEFT, UPRIGHT, DOWNLEFT, DOWNRIGHT, UP, DOWN, LEFT, RIGHT]

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
    def __init__(self, x, y, width, height):
        self.bilde = pygame.image.load("Ild.png").convert_alpha()
        self.bilde = pygame.transform.scale(self.bilde, (width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.retning = random.choice(RETNINGER)

        
    def beveg(self):
        # Flytter ildkulene basert på nåværende retning
        if self.retning == DOWNLEFT:
            self.rect.left -= MOVESPEED
            self.rect.top += MOVESPEED
        elif self.retning == DOWNRIGHT:
            self.rect.left += MOVESPEED
            self.rect.top += MOVESPEED
        elif self.retning == UPLEFT:
            self.rect.left -= MOVESPEED
            self.rect.top -= MOVESPEED
        elif self.retning == UPRIGHT:
            self.rect.left += MOVESPEED
            self.rect.top -= MOVESPEED
        elif self.retning == LEFT:
            self.rect.left += MOVESPEED
        elif self.retning == RIGHT:
            self.rect.left -= MOVESPEED
        elif self.retning == UP:
            self.rect.top -= MOVESPEED
        elif self.retning == DOWN:
            self.rect.top += MOVESPEED
        
            
    def check_bounds(self, width, height):
        #Sjekker og korrigerer blokkens posisjon når den treffer kantene.
        if self.rect.top < -50:
            # Ildkula har gått over toppen
            if self.retning == UPLEFT:
                self.retning = DOWNLEFT
            elif self.retning == UPRIGHT:
                self.retning = DOWNRIGHT
            elif self.retning == UP:
                self.retning = DOWN
        if self.rect.bottom > vinduy + 50:
            # Ildkula har gått under bunnen
            if self.retning == DOWNLEFT:
                self.retning = UPLEFT
            elif self.retning == DOWNRIGHT:
                self.retning = UPRIGHT
            elif self.retning == DOWN:
                self.retning = UP
        if self.rect.left < -50:
            # Ildkula har gått over venstre siden
            if self.retning == DOWNLEFT:
                self.retning = DOWNRIGHT
            elif self.retning == UPLEFT:
                self.retning = UPRIGHT
            elif self.retning == LEFT:
                self.retning = RIGHT
        if self.rect.right > vindux + 50:
            # Ildkula har gått over høyresiden
            if self.retning == DOWNRIGHT:
                self.retning = DOWNLEFT
            elif self.retning == UPRIGHT:
                self.retning = UPLEFT
            elif self.retning == RIGHT:
                self.retning = LEFT 
            
        
    def tegn(self, overflate):
        overflate.blit(self.bilde, (self.rect.x, self.rect.y))
        
# Oppretter de første ildkulene
ildkuler = [ild(random.randint(0, vindux - 50), random.randint(0, vinduy - 50), 50, 50) for _ in range(2)]

# Tid for å legge til nye ildkuler
pluss_intervall = 3000 # 3000 ms/3 s
sist_pluss = pygame.time.get_ticks()


# Hovedspill løkke
clock = pygame.time.Clock()
run = True
while run:
    # Avslutter spillet hvis slutt hendelse
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            
    # Oppdaterer ildkulene
    for ildkule in ildkuler:
        ildkule.beveg()
        ildkule.check_bounds(vindux, vinduy)
        
    # Legger til nye ildkuler etter en viss tid
    gjeldende_tid = pygame.time.get_ticks()
    if gjeldende_tid - sist_pluss >= pluss_intervall:
        ildkuler.append(ild(random.randint(0, vindux - 50), random.randint(0, vinduy - 50), 50, 50))
        sist_pluss = gjeldende_tid # Oppdaterer siste tid en ildkule ble lagt til
        
    # Fjerner bakgrunnen        
    overflate.fill((0, 0, 0))
        
    # Tegner bakgrunnene
    overflate.blit(t_bg1, (0, 0))
    overflate.blit(t_bg2, (0, 0))
    overflate.blit(t_bg3, (0, 0))
    overflate.blit(t_bg4, (0, 0))
    
    # Tegner ildkulene
    for ildkule in ildkuler:
        ildkule.tegn(overflate)
    
    # Opptaterer skjermen
    pygame.display.update()
    
    # Setter FPS (frames per second)
    clock.tick(60)

# Avslutter pygame
pygame.quit()

