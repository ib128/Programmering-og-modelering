#PLAN: Person som prøver å unngå å bli truffet av fireballs eller annet
# Jo lengre du holder ut jo mer poeng tjener du + økende vanskelighet
# mulige "upgrades"?

import pygame

# Vindustørrelse
vindux = 800 #576
vinduy = 600 #324

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

# Definerer spillerklassen
class player:
    def __init__(self, x, y, width, height):
        self.bilde = pygame.image.load("Slime_idle.png").convert_alpha()
        self.bilde = pygame.transform.scale(self.bilde, (width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.dx = 7
        self.dy = 7
        
    def tegn(self):
        overflate.blit(self.bilde, (self.rect.x, self.rect.y))

    def beveg(self, keys):
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.dx
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.dx
        if keys[pygame.K_UP]:
            self.rect.y -= self.dy
        if keys[pygame.K_DOWN]:
            self.rect.y += self.dy
            
# Definerer fiendeklassen (ildkuler)          
            
        
# Lager spillerobjekt
spiller = player(300, 300, 50, 50)

# Spill løkke
clock = pygame.time.Clock()
run = True
while run:
    #Avslutter spillet
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    # Beveger spilleren hvis riktig knapper er presset      
    keys = pygame.key.get_pressed()
    spiller.beveg(keys)
                
    # Fjerner bakgrunnen        
    overflate.fill((0, 0, 0))
        
    # Tegner bakgrunnene
    overflate.blit(t_bg1, (0, 0))
    overflate.blit(t_bg2, (0, 0))
    overflate.blit(t_bg3, (0, 0))
    overflate.blit(t_bg4, (0, 0))
    
    # Tegner spilleren
    spiller.tegn()

    # Opptaterer skjermen
    pygame.display.update()
    
    # Setter FPS (frames per second)
    clock.tick(60)

# Avslutter pygame
pygame.quit()