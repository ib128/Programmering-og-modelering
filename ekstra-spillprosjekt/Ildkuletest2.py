import pygame
import random

# Vindustørrelse
vindux = 800 #576
vinduy = 600 #324

# Ildkulefarten 
MOVESPEED = 7

# Retninger som vektorer
RETNINGER = [
    (-1, -1),  # UPLEFT
    (1, -1),   # UPRIGHT
    (-1, 1),   # DOWNLEFT
    (1, 1),    # DOWNRIGHT
    (0, -1),   # UP
    (0, 1),    # DOWN
    (-1, 0),   # LEFT
    (1, 0)]    # RIGHT

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
        self.endre_timer = random.randint(30, 120) # hvor ofte endre retning
        self.timer = 0
        
    def beveg(self):
        # Beveger ildkulene i retningen
        self.rect.x += self.retning[0] * MOVESPEED
        self.rect.x += self.retning[1] * MOVESPEED
        
        # Øker timer
        self.timer += 1
            
        # Endrer retning når timeren når grensen
        if self.timer >= self.endre_timer:
            self.retning = random.choice(RETNINGER)
            self.timer = 0 
            
    def check_bounds(self, width, height):
        #Sjekker og korrigerer blokkens posisjon når den treffer kantene.
        if self.rect.top < -100:
            # Ildkula har gått over toppen
            self.retning = (self.retning[0], -self.retning[1])
        if self.rect.bottom > height + 100:
            # Ildkula har gått under bunnen
            self.retning = (self.retning[0], -self.retning[1])
        if self.rect.left < -100:
            # Ildkula har gått over venstre siden
            self.retning = (-self.retning[0], self.retning[1])
        if self.rect.right > width + 100:
            # Ildkula har gått over høyresiden
            self.retning = (self.retning[0], -self.retning[1])
            
        
    def tegn(self, overflate):
        overflate.blit(self.bilde, (self.rect.x, self.rect.y))
        
# Opprett ildkulene
ildkuler = [ild(random.randint(0, vindux - 50), random.randint(0, vinduy - 50), 50, 50) for _ in range(10)]


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
