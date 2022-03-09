import pygame
import time

def glowstone() :
    FPS = 60
    SPEED = 5
    '''
    Template :
    '''

    class Player:
        def __init__(self,x ,y) :
            self.image = pygame.image.load(f'Nemegis/texture/player.png')
            self.rect = self.image.get_rect(x=x, y=y)
            self.speed = SPEED
            self.velocity = [0, 0]
        
        def move(self) :
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

        def draw(self, screen) :
            screen.blit(self.image, self.rect)
    
    class Pnjeather:
        def __init__(self,x ,y) :
            self.image = pygame.image.load(f'Nemegis/texture/quest-eather.png')
            self.rect = self.image.get_rect(x=x, y=y)
            self.speed = SPEED
            self.velocity = [0, 0]
        
        def move(self) :
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

        def draw(self, screen) :
            screen.blit(self.image, self.rect)

    class Overworld:
        def __init__(self,x ,y) :
            self.image = pygame.image.load(f'Nemegis/texture/quest1.png')
            self.rect = self.image.get_rect(x=x, y=y)
            self.speed = 15
            self.velocity = [0, 0]
        
        def move(self) :
            self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

        def draw(self, screen) :
            screen.blit(self.image, self.rect)

    '''
    End of Template
    '''

    class Game:
        
        def __init__(self, screen):
            self.screen = screen
            self.running = True
            self.clock = pygame.time.Clock()
            self.player = Player(720, 420)
            self.background = Overworld(0,0)
            self.direction = 1
            self.temp=0
            self.diag=Pnjeather(100,600)
            self.affichage = False
            
        def handling_event(self):
            for event in pygame.event.get() :
                    if event.type == pygame.QUIT :
                        self.running = False
            key = pygame.key.get_pressed()

                ############   Bouger   ##############
            if key[pygame.K_z] :
                self.player.velocity[1] = -1
                self.player.velocity[0] = 0
            elif key[pygame.K_s] :
                self.player.velocity[1] = 1
                self.player.velocity[0] = 0
            elif key[pygame.K_d] :
                self.player.velocity[0] = 1
                self.player.velocity[1] = 0
            elif key[pygame.K_q] :
                self.player.velocity[0] = -1
                self.player.velocity[1] = 0
            else : 
                self.player.velocity[1] = 0
                self.player.velocity[0] = 0

                ############   Colision   ############
            if self.player.rect.x < 0 :
                self.player.rect.x = 5
            if self.player.rect.x > 840 :
                self.player.rect.x = 835
            if self.player.rect.y < 0 :
                self.player.rect.y = 5
            if self.player.rect.y > 840 :
                self.player.rect.y = 835
            
            if True :
        #maison 1
                if 740 <= self.player.rect.x <= 900 and 340 <= self.player.rect.y <= 470 :
                    if key[pygame.K_SPACE] :
                        from main import map
                        map()
            if self.temp%60 == 0 :
                print('------------------')
                print('x : ', self.player.rect.x)
                print('y : ',self.player.rect.y)
                print('------------------')

            if  350 <= self.player.rect.x <= 365 and 355 <= self.player.rect.y <= 475 :
                self.player.rect.x -= SPEED 
            if  350-SPEED <= self.player.rect.x <= 365-SPEED and 355 <= self.player.rect.y <= 475 :
                if key[pygame.K_f] :
                    self.affichage = self.affichage ^ True
                    time.sleep(0.2)
            
            if  480 <= self.player.rect.x <= 485 and 355 <= self.player.rect.y <= 475 :
                self.player.rect.x += SPEED 
            if  480+SPEED <= self.player.rect.x <= 485+SPEED and 355 <= self.player.rect.y <= 475 :
                if key[pygame.K_f] :
                    self.affichage = self.affichage ^ True
                    time.sleep(0.2)

                





        def update(self) :
            self.player.move()

        def display(self) :

            self.background.draw(self.screen)
            self.player.draw(self.screen)
            if self.affichage == True :
                self.diag.draw(self.screen)

            pygame.display.flip()

        def run(self) :
            while self.running :
                self.handling_event()
                self.update()
                self.display()
                self.clock.tick(FPS)
                self.temp+=1


    pygame.init()
    screen = pygame.display.set_mode((900, 900))
    Game = Game(screen)
    Game.run()


    pygame.quit()

