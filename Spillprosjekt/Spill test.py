#PLAN: Person som prøver å unngå å bli truffet av fireballs eller annet
# Jo lengre du holder ut jo mer poeng tjener du + økende vanskelighet
# mulige "upgrades"?

import pygame

# Vindustørrelse
vindux = 640 #576
vinduy = 480 #324

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
        self.spillerx= x
        self.spillery = y
        self.dx = 10
        self.dy = 10
        
    def tegn(self):
        overflate.blit(self.spiller, (self.spillerx, self.spillery))

        
    def right(self):
        self.spillerx += self.dx
    def left(self):
        self.spillerx -= self.dx
    def up(self):
        self.spillery -= self.dy
    def down(self):
        self.spillery += self.dy
        
# Lageer spillerobjekt
spiller = player(300, 300)

# Spill løkke
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                spiller.right()
            if e.key == pygame.K_LEFT:
                spiller.left()
            if e.key == pygame.K_UP:
                spiller.up()
            if e.key == pygame.K_DOWN:
                spiller.down()
                
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