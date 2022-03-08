import pygame

FPS = 60

'''
Template :
'''

class Player:
    def __init__(self,x ,y) :
        self.image = pygame.image.load(f'Nemegis/texture/player.png')
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 10
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
        
    def handling_event(self):
        for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    self.running = False
        key = pygame.key.get_pressed()

            ############   Bouger   ##############
        if key[pygame.K_z] :
            self.player.velocity[1] = -1
        elif key[pygame.K_s] :
            self.player.velocity[1] = 1
        elif key[pygame.K_d] :
            self.player.velocity[0] = 1
        elif key[pygame.K_q] :
            self.player.velocity[0] = -1
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

pygame.init()
screen = pygame.display.set_mode((900, 900))
Game = Game(screen)
Game.run()


pygame.quit()