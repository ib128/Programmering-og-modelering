#PLAN: Person som prøver å unngå å bli truffet av fireballs eller annet
# Jo lengre du holder ut jo mer poeng tjener du + økende vanskelighet
# mulige "upgrades"?

import pygame
vindux = 640 #576
vinduy = 480 #324

#initiering av programmet
pygame.init()
overflate = pygame.display.set_mode((vindux, vinduy))
pygame.display.set_caption("Spill test")

#importerer bakgrunnsbildene
bg1 = pygame.image.load("BG/Clouds1/1.png")
bg2 = pygame.image.load("BG/Clouds1/2.png")
bg3 = pygame.image.load("BG/Clouds1/3.png")
bg4 = pygame.image.load("BG/Clouds1/4.png")
#tilpasser bakrunn til vinduet
t_bg1 = pygame.transform.scale(bg1, (vindux, vinduy))
t_bg2 = pygame.transform.scale(bg2, (vindux, vinduy))
t_bg3 = pygame.transform.scale(bg3, (vindux, vinduy))
t_bg4 = pygame.transform.scale(bg4, (vindux, vinduy))

#plasserer inn bakgrunnsbildene
overflate.blit(t_bg1, (0, 0))
overflate.blit(t_bg2, (0, 0))
overflate.blit(t_bg3, (0, 0))
overflate.blit(t_bg4, (0, 0))

pygame.display.update()

class spiller:
    def __init__(self, x, y):
        global spillerx, spillery, spiller
        spiller = pygame.image.load(..)
        spillerx= x
        spillery = y
        dx = dy = 10
        overflate.blit(spiller, (spillerx, spillery))
        pygame.display.update()
        
    def right(self):
        spillerx = spillerx + dx
    def left(self):
        spillerx = spillerx - dx
    def up(self):
        spillery = spillery + y
    def down(self):
        spillery = spillery - y

run = True
while run:
    for e in pygame.event.get():
        if e.key == pygame.K_RIGHT:
            spiller.right()
        if e.key == pygame.K_LEFT:
            spiller.left()
        if e.key == pygame.K_UP:
            spiller.up()
        if e.key == pygame.K_DOWN:
            spiller.down()
        
    
    


while True: #Så lenge denne er sann, og det er den
    for e in pygame.event.get():
        # henter alle hendelser fra mus og tastatur
        if e.type == pygame.QUIT: #sjekker om en hendelse var avslutt
            pygame.quit() # dersom det var det, avsluttes programmet
    pygame.display.update()

