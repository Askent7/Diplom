import pygame

class Player_Hive(pygame.sprite.Sprite):
    def __init__(self, x_center, y_center, type, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            img).convert_alpha()
        self.rect = self.image.get_rect(
            center=(x_center,y_center))
        self.mas = None
        self.x_center = x_center
        self.y_center = y_center
        self.type = type
    
    def update_pos(self, x_center, y_center, mas):
        self.mas = mas
        self.x_center = x_center
        self.y_center = y_center       
        self.rect = self.image.get_rect(
            center=(x_center,y_center))
        
class Player_Hive_Beatle(pygame.sprite.Sprite):
    def __init__(self, x_center, y_center, type, img, id):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            img).convert_alpha()
        self.rect = self.image.get_rect(
            center=(x_center,y_center))
        self.mas = None
        self.x_center = x_center
        self.y_center = y_center
        self.type = type
        self.id = id
    
    def update_pos(self, x_center, y_center, mas):
        self.mas = mas
        self.x_center = x_center
        self.y_center = y_center       
        self.rect = self.image.get_rect(
            center=(x_center,y_center))
    def update_img(self, img):
        self.image = pygame.image.load(
            img).convert_alpha()
    