import pygame

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

class Overworld:
    def __init__(self,x ,y) :
        self.image = pygame.image.load(f'Nemegis/texture/overword.png')
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
        self.player = Player(420, 820)
        self.background = Overworld(0,0)
        self.direction = 1
        self.temp=0
        
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
            if  40 <= self.player.rect.x <= 45 and 740 <= self.player.rect.y <= 900 :
                self.player.rect.x -= SPEED
            if  195 <= self.player.rect.x <= 200 and 740 <= self.player.rect.y <= 900 :
                self.player.rect.x += SPEED
            if  740 <= self.player.rect.y <= 745 and 40 <= self.player.rect.x <= 200 :
                self.player.rect.y -= SPEED
    #maison 2
            if  40 <= self.player.rect.x <= 45 and 540 <= self.player.rect.y <= 700 :
                self.player.rect.x -= SPEED
            if  195 <= self.player.rect.x <= 200 and 540 <= self.player.rect.y <= 700 :
                self.player.rect.x += SPEED
                if key[pygame.K_SPACE] :
                    print('ça marche')
            if  700 <= self.player.rect.y <= 705 and 40 <= self.player.rect.x <= 200 :
                self.player.rect.y += SPEED
            if  540 <= self.player.rect.y <= 545 and 40 <= self.player.rect.x <= 200 :
                self.player.rect.y -= SPEED
    #maison 3
            if  40 <= self.player.rect.x <= 45 and 340 <= self.player.rect.y <= 500 :
                self.player.rect.x -= SPEED
            if  195 <= self.player.rect.x <= 200 and 340 <= self.player.rect.y <= 500 :
                self.player.rect.x += SPEED
            if  340 <= self.player.rect.y <= 345 and 40 <= self.player.rect.x <= 200 :
                self.player.rect.y -= SPEED
            if  495 <= self.player.rect.y <= 500 and 40 <= self.player.rect.x <= 200 :
                self.player.rect.y += SPEED
    #maison 4
            if  40 <= self.player.rect.x <= 45 and 140 <= self.player.rect.y <= 300 :
                self.player.rect.x -= SPEED
            if  195 <= self.player.rect.x <= 200 and 140 <= self.player.rect.y <= 300 :
                self.player.rect.x += SPEED
            if  295 <= self.player.rect.y <= 300 and 40 <= self.player.rect.x <= 200 :
                self.player.rect.y += SPEED
            if  140 <= self.player.rect.y <= 145 and 40 <= self.player.rect.x <= 200 :
                self.player.rect.y -= SPEED

    #maison 1
            if  640 <= self.player.rect.x <= 645 and 740 <= self.player.rect.y <= 900 :
                self.player.rect.x -= SPEED
            if  795 <= self.player.rect.x <= 800 and 740 <= self.player.rect.y <= 900 :
                self.player.rect.x += SPEED
            if  740 <= self.player.rect.y <= 745 and 640 <= self.player.rect.x <= 800 :
                self.player.rect.y -= SPEED
    #maison 2
            if  640 <= self.player.rect.x <= 645 and 540 <= self.player.rect.y <= 700 :
                self.player.rect.x -= SPEED
                if key[pygame.K_SPACE] :
                    print('ça marche')
            if  795 <= self.player.rect.x <= 800 and 540 <= self.player.rect.y <= 700 :
                self.player.rect.x += SPEED
            if  700 <= self.player.rect.y <= 705 and 640 <= self.player.rect.x <= 800 :
                self.player.rect.y += SPEED
            if  540 <= self.player.rect.y <= 545 and 640 <= self.player.rect.x <= 800 :
                self.player.rect.y -= SPEED
    #maison 3
            if  640 <= self.player.rect.x <= 645 and 340 <= self.player.rect.y <= 500 :
                self.player.rect.x -= SPEED
            if  195+600 <= self.player.rect.x <= 200+600 and 340 <= self.player.rect.y <= 500 :
                self.player.rect.x += SPEED
            if  340 <= self.player.rect.y <= 345 and 40+600 <= self.player.rect.x <= 200+600 :
                self.player.rect.y -= SPEED
            if  495 <= self.player.rect.y <= 500 and 40+600 <= self.player.rect.x <= 200+600 :
                self.player.rect.y += SPEED
    #maison 4
            if  40+600 <= self.player.rect.x <= 45+600 and 140 <= self.player.rect.y <= 300 :
                self.player.rect.x -= SPEED
            if  195+600 <= self.player.rect.x <= 200+600 and 140 <= self.player.rect.y <= 300 :
                self.player.rect.x += SPEED
            if  295 <= self.player.rect.y <= 300 and 40+600 <= self.player.rect.x <= 200+600 :
                self.player.rect.y += SPEED
            if  140 <= self.player.rect.y <= 145 and 40+600 <= self.player.rect.x <= 200+600 :
                self.player.rect.y -= SPEED
    #maison 1
            if  140 <= self.player.rect.x <= 145 and 40 <= self.player.rect.y <= 200 :
                self.player.rect.x -= SPEED
            if  295 <= self.player.rect.x <= 300 and 40 <= self.player.rect.y <= 200 :
                self.player.rect.x += SPEED
            if  40 <= self.player.rect.y <= 45 and 140 <= self.player.rect.x <= 300 :
                self.player.rect.y -= SPEED
            if  195 <= self.player.rect.y <= 200 and 140 <= self.player.rect.x <= 300 :
                self.player.rect.y += SPEED

    #maison 2
            if  140+200 <= self.player.rect.x <= 145+200 and 40 <= self.player.rect.y <= 200 :
                self.player.rect.x -= SPEED
            if  295+200 <= self.player.rect.x <= 300+200 and 40 <= self.player.rect.y <= 200 :
                self.player.rect.x += SPEED
            if  40 <= self.player.rect.y <= 45 and 140+200 <= self.player.rect.x <= 300+200 :
                self.player.rect.y -= SPEED
            if  195 <= self.player.rect.y <= 200 and 140+200 <= self.player.rect.x <= 300+200 :
                self.player.rect.y += SPEED
                if key[pygame.K_SPACE] :
                    print('ça marche')

    #maison 3
            if  140+400 <= self.player.rect.x <= 145+400 and 40 <= self.player.rect.y <= 200 :
                self.player.rect.x -= SPEED
            if  295+400 <= self.player.rect.x <= 300+400 and 40 <= self.player.rect.y <= 200 :
                self.player.rect.x += SPEED
            if  40 <= self.player.rect.y <= 45 and 140+400 <= self.player.rect.x <= 300+400 :
                self.player.rect.y -= SPEED
            if  195 <= self.player.rect.y <= 200 and 140+400 <= self.player.rect.x <= 300+400 :
                self.player.rect.y += SPEED
            
    
        if self.temp%60 == 0 :
            print('------------------')
            print('x : ', self.player.rect.x)
            print('y : ',self.player.rect.y)
            print('------------------')

            





    def update(self) :
        self.player.move()

    def display(self) :
        self.screen.fill('black')
        self.background.draw(self.screen)
        self.player.draw(self.screen)

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