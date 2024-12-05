#PLAN: Person som prøver å unngå å bli truffet av bomber/kniver/ett eller annet
# Jo lengre du holder ut jo mer poeng tjener du + økende vanskelighet
# mulige "upgrades"

import pygame

#initiering av programmet
pygame.init()
overflate = pygame.display.set_mode((248, 208))
pygame.display.set_caption("Spill test")

bg = pygame.image.load("Rom1.png")
overflate.blit(bg, (0, 0))
pygame.display.update()


while True: #Så lenge denne er sann, og det er den
    for e in pygame.event.get():
        # henter alle hendelser fra mus og tastatur
        if e.type == pygame.QUIT: #sjekker om en hendelse var avslutt
            pygame.quit() # dersom det var det, avsluttes programmet
    pygame.display.update()
            