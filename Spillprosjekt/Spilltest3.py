import pygame
import random

# Vindustørrelse
vindux = 800 #576
vinduy = 600 #324

# Spill variabler
meny = True
alive = False
run = True
slutt_tid = 0

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

#Game over bakgrunnsbilde
gameover_bg = pygame.image.load("BG/Gameover_bg.png")

# Tilpasser bakrunnen til vinduet
t_bg1 = pygame.transform.scale(bg1, (vindux, vinduy))
t_bg2 = pygame.transform.scale(bg2, (vindux, vinduy))
t_bg3 = pygame.transform.scale(bg3, (vindux, vinduy))
t_bg4 = pygame.transform.scale(bg4, (vindux, vinduy))
gameover_bg = pygame.transform.scale(gameover_bg, (vindux, vinduy))

def timer():
    if spiller.is_dead:
        text = "Tid: " + str(final_tid) + "s"
    else:
        elapsed_time = (pygame.time.get_ticks() - start_tid) // 1000
        font = pygame.font.Font("PressStart2P.ttf", 30)
        text = "Tid: " + str(elapsed_time) + "s"
    
    font = pygame.font.Font("PressStart2P.ttf", 30)
    Timer = font.render(text, True, (225, 255, 225))
    overflate.blit(Timer, (10, 10))


# Definerer spillerklassen
class player:
    def __init__(self, x, y, width, height):
        self.bilde = pygame.image.load("Slime_idle.png").convert_alpha()
        self.bilde = pygame.transform.scale(self.bilde, (width, height))
        self.rect = pygame.Rect(x, y, width, height)
        
        # Reduserer spillerens kollisjonsboks
        self.kollisjon_rect = pygame.Rect(self.rect.x + 10, self.rect.y + 15, self.rect.width - 20, self.rect.height - 20)
        
        self.dx = 7
        self.dy = 7
        
        # Dødsanimasjonsvariabler
        sprite_sheet = pygame.image.load("Slime1_Death_body.png").convert_alpha()
        self.death_frames = self.hent_rammer(sprite_sheet, 10, 64, 64)
        self.current_frame = 0
        self.is_dead = False
        self.animation_done = False
        self.animation_speed = 100
        self.last_frame_time = 0
        
    def hent_rammer(self, sprite_sheet, antall_rammer, rammebredde, rammehøyde):
        rammer = []
        for i in range(antall_rammer):
            frame = sprite_sheet.subsurface((i*rammebredde, 0, rammebredde, rammehøyde))
            rammer.append(frame)
        return rammer
        
    # Flytter spilleren basert på tastatur klikk
    def beveg(self, keys):
        if not self.is_dead:
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.dx
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.dx
            if keys[pygame.K_UP]:
                self.rect.y -= self.dy
            if keys[pygame.K_DOWN]:
                self.rect.y += self.dy
            
            #Oppdaterer kollisjonsbpoksen etter bevegelse
            self.kollisjon_rect.topleft = (self.rect.x + 10, self.rect.y + 15)
           
    def check_bounds(self, width, height):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
        
    def tegn(self):
        overflate.blit(self.bilde, (self.rect.x, self.rect.y))
    
    def play_death_animation(self, ildkuler, bakgrunner):
        # Spiller dødsanimasjonen en gang
        if not self.animation_done:
            now = pygame.time.get_ticks()
            if now - self.last_frame_time > self.animation_speed:
                self.last_frame_time = now
                
                for bg in bakgrunner:
                    overflate.blit(bg,(0,0))
                    
                for ildkule in ildkuler:
                    ildkule.tegn(overflate)
                
                if self.current_frame < len(self.death_frames):
                    overflate.blit(self.death_frames[self.current_frame], (self.rect.x, self.rect.y))
                    self.current_frame += 1
                else:
                    self.animation_done = True
        else:
            # Tegner siste frame som stillebilde etter animasjonen er ferdig
            for bg in bakgrunner:
                overflate.blit(bg,(0,0))       
            for ildkule in ildkuler:
                ildkule.tegn(overflate)
                    
            overflate.blit(self.death_frames[-1], (self.rect.x, self.rect.y))

# Definerer fiendeklassen (ildkuler)
class ild:
    def __init__(self, x, y, width, height, spiller):
        self.bilde = pygame.image.load("Ild.png").convert_alpha()
        self.bilde = pygame.transform.scale(self.bilde, (width, height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.spiller = spiller
        
        # Velg en tilfeldig kant for spawn
        self.rect = self.ildkule_spawn_posisjon()

        # Velger en tilfeldig retning
        self.retning = random.choice(RETNINGER)
        
        # Reduserer ildkulenes kollisjonsboks
        self.kollisjon_rect = pygame.Rect(self.rect.x + 15, self.rect.y + 15, self.rect.width - 35, self.rect.height - 35)

    def ildkule_spawn_posisjon(self):
        # Velger en tilfeldig kant å plassere ildkule
        while True:
            kant = random.choice(["topp", "bunn", "venstre", "høyre"])
            
            if kant == "topp":
                bredde = random.randint(0, self.width)
                høyde = self.height
            elif kant == "bunn":
                bredde = random.randint(0, self.width)
                høyde = vinduy
            elif kant == "venstre":
                bredde = -self.width
                høyde = random.randint(0, vinduy)
            elif kant == "høyre":
                bredde = vindux
                høyde = random.randint(0, vinduy)
                
            ny_rektangel = pygame.Rect(bredde, høyde, self.width, self.height)
            
            # Sjekker at ildkulen ikke overlapper med spilleren
            if not ny_rektangel.colliderect(self.spiller.rect):
                return ny_rektangel
            
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
            self.rect.left -= MOVESPEED
        elif self.retning == RIGHT:
            self.rect.left += MOVESPEED
        elif self.retning == UP:
            self.rect.top -= MOVESPEED
        elif self.retning == DOWN:
            self.rect.top += MOVESPEED
        
        #Oppdaterer kollisjonsboksen etter bevegelse
        self.kollisjon_rect.topleft = (self.rect.x + 15, self.rect.y + 15)
            
    def check_bounds(self, width, height):
        #Sjekker og korrigerer blokkens posisjon når den treffer kantene.
        if self.rect.top < -100:
            # Ildkula har gått over toppen
            if self.retning == UPLEFT:
                self.retning = DOWNLEFT
            elif self.retning == UPRIGHT:
                self.retning = DOWNRIGHT
            elif self.retning == UP:
                self.retning = DOWN
        if self.rect.bottom > height + 100:
            # Ildkula har gått under bunnen
            if self.retning == DOWNLEFT:
                self.retning = UPLEFT
            elif self.retning == DOWNRIGHT:
                self.retning = UPRIGHT
            elif self.retning == DOWN:
                self.retning = UP
        if self.rect.left < -100:
            # Ildkula har gått over venstre siden
            if self.retning == DOWNLEFT:
                self.retning = DOWNRIGHT
            elif self.retning == UPLEFT:
                self.retning = UPRIGHT
            elif self.retning == LEFT:
                self.retning = RIGHT
        if self.rect.right > width + 100:
            # Ildkula har gått over høyresiden
            if self.retning == DOWNRIGHT:
                self.retning = DOWNLEFT
            elif self.retning == UPRIGHT:
                self.retning = UPLEFT
            elif self.retning == RIGHT:
                self.retning = LEFT 
            
        
    def tegn(self, overflate):
        overflate.blit(self.bilde, (self.rect.x, self.rect.y))
        
# Lager spillerobjekt
spiller = player(300, 300, 50, 50)

# Oppretter de første ildkulene
ildkuler = [ild(vindux, vinduy, 60, 60, spiller) for _ in range(5)]

# Tid for å legge til nye ildkuler
pluss_intervall = 5000 # 5000 ms/5 s
sist_pluss = pygame.time.get_ticks()

# Hovedspill løkke
clock = pygame.time.Clock()
# Setter FPS (frames per second)
clock.tick(60)
while run:
    if meny:
        # Tegner bakgrunnene
        overflate.blit(t_bg1, (0, 0))
        overflate.blit(t_bg2, (0, 0))
        overflate.blit(t_bg3, (0, 0))
        overflate.blit(t_bg4, (0, 0))
        
        font1 = pygame.font.Font("PressStart2P.ttf", 60)
        skygge1F = pygame.font.Font("PressStart2P.ttf", 60)
        font2 = pygame.font.Font("PressStart2P.ttf", 20)
        
        tekst1 = font1.render("Fireball", True, (255, 255, 255))
        skygge1 = skygge1F.render("Fireball", True, (255, 69, 0))
        tekst2 = font2.render("Trykk 'R' for å starte spillet", True, (255, 69, 0))
        
        # Sentral plassering
        tekst1_x = vindux // 2 - tekst1.get_width() // 2
        tekst1_y = vinduy // 2 - tekst1.get_height() // 2
        
        offset = 3  # Skyggeforskyvning
        
        # Tegner skyggen på alle sider for å skape border
        overflate.blit(skygge1, (tekst1_x - offset, tekst1_y))
        overflate.blit(skygge1, (tekst1_x + offset, tekst1_y))
        overflate.blit(skygge1, (tekst1_x, tekst1_y - offset))
        overflate.blit(skygge1, (tekst1_x, tekst1_y + offset))
        
        # Tegner selve teksten i midten av skyggene
        overflate.blit(tekst1, (tekst1_x, tekst1_y))
        overflate.blit(tekst2, (vindux // 2 - tekst2.get_width() // 2, (vinduy // 2 - tekst2.get_height() // 2) + 100))
        
        pygame.display.update()
        
       #Avslutter spillet
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
            alive = True
            meny = False
            start_tid = pygame.time.get_ticks()
    
    if alive:
        # Oppdaterer ildkulene
        for ildkule in ildkuler:
            ildkule.beveg()
            ildkule.check_bounds(vindux, vinduy)
            # Kollisjonsjekk mellom spiller og ildkuler
            if spiller.kollisjon_rect.colliderect(ildkule.kollisjon_rect):
                spiller.is_dead = True
                alive = False
                final_tid = (pygame.time.get_ticks() - start_tid) // 1000 # Lagrer sluttid
        
        # Legger til nye ildkuler etter en viss tid
        gjeldende_tid = pygame.time.get_ticks()
        if gjeldende_tid - sist_pluss >= pluss_intervall:
            ildkuler.append(ild(random.randint(0, vindux - 50), random.randint(0, vinduy - 50), 60, 60, spiller))
            sist_pluss = gjeldende_tid # Oppdaterer siste tid en ildkule ble lagt til
        
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
        
        # Lager timer
        timer()
        
        # Tegner spilleren
        spiller.tegn()
        # Sjekker at spilleren ikke er utenfor skjermen
        spiller.check_bounds(vindux, vinduy)
        
        # Tegner ildkulene
        for ildkule in ildkuler:
            ildkule.tegn(overflate)
        
        # Opptaterer skjermen
        pygame.display.update()
        
    elif spiller.is_dead:
        if not spiller.animation_done:
            spiller.play_death_animation(ildkuler, [t_bg1, t_bg2, t_bg3, t_bg4])
            pygame.display.update()
        else:
            # Spilleren er død, tegner "Game Over"-skjerm
            overflate.fill((0, 0, 0))
            overflate.blit(gameover_bg, (0, 0))
            
            font1 = pygame.font.Font("PressStart2P.ttf", 60)
            font2 = pygame.font.Font("PressStart2P.ttf", 20)
            
            tekst1 = font1.render("Game Over", True, (255, 255, 255))
            tekst2 = font2.render("Trykk 'R' for å prøve igjen", True, (255, 255, 255))
            overflate.blit(tekst1, (vindux // 2 - tekst1.get_width() // 2, vinduy // 2 - tekst1.get_height() // 2))
            overflate.blit(tekst2, (vindux // 2 - tekst2.get_width() // 2, (vinduy // 2 - tekst2.get_height() // 2) + 100))
            timer() # printer slutt-tid
            pygame.display.update()
            
            # Venter på spill-avslutning eller restart
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:  # Restart med "R"
                alive = True
                ildkuler = [ild(vindux, vinduy, 60, 60, spiller) for _ in range(5)]
                spiller = player(300, 300, 50, 50)

# Avslutter pygame
pygame.quit()