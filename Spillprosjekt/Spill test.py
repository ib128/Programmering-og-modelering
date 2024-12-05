#PLAN: Person som prøver å unngå å bli truffet av fireballs eller annet
# Jo lengre du holder ut jo mer poeng tjener du + økende vanskelighet
# mulige "upgrades"?

import pygame

#initiering av programmet
pygame.init()
overflate = pygame.display.set_mode((576, 324))
pygame.display.set_caption("Spill test")

bg1 = pygame.image.load("BG/Clouds1/1.png")
bg2 = pygame.image.load("BG/Clouds1/2.png")
bg3 = pygame.image.load("BG/Clouds1/3.png")
bg4 = pygame.image.load("BG/Clouds1/4.png")

overflate.blit(bg1, (0, 0))
overflate.blit(bg2, (0, 0))
overflate.blit(bg3, (0, 0))
overflate.blit(bg4, (0, 0))

pygame.display.update()


while True: #Så lenge denne er sann, og det er den
    for e in pygame.event.get():
        # henter alle hendelser fra mus og tastatur
        if e.type == pygame.QUIT: #sjekker om en hendelse var avslutt
            pygame.quit() # dersom det var det, avsluttes programmet
    pygame.display.update()

