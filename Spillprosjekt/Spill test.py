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

# Definerer spillerklasse
class player:
    def __init__(self, x, y):
        self.spiller = pygame.image.load("Slime_idle.png").convert_alpha()
        self.spiller = pygame.transform.scale(self.spiller, (50, 50))
        self.spillerx= x
        self.spillery = y
        self.dx = 10
        self.dy = 10
        
    def tegn(self):
        overflate.blit(self.spiller, (self.spillerx, self.spillery))

    def beveg(self, keys):
        if keys[pygame.K_RIGHT]:
            self.spillerx += self.dx
        if keys[pygame.K_LEFT]:
            self.spillerx -= self.dx
        if keys[pygame.K_UP]:
            self.spillery -= self.dy
        if keys[pygame.K_DOWN]:
            self.spillery += self.dy
            
        
# Lager spillerobjekt
spiller = player(300, 300)

# Spill løkke
run = True
while run:
    #Avslutter spillet
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            
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
    pygame.time.Clock().tick(60)

# Avslutter pygame
pygame.quit()