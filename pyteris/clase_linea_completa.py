import pygame 

linea_completa = pygame.sprite.Group()



class animacion_linea(pygame.sprite.Sprite):
    def __init__(self,altura_linea_completa:int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r"imagenes\linea completa.png")
        self.rect = self.image.get_rect()
        self.centerx = 240
        self.centery = altura_linea_completa
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        self.frame_rate = 10
        self.frame = 0
        self.contador = 0


    def update(self):
        if self.contador == self.frame_rate:
            self.rect.scale_by_ip(0.6)
            self.rect.centerx = self.centerx
            self.image = pygame.transform.scale_by(self.image,0.8)
            
        else:
            self.contador += 1

        if self.frame == 6:
            self.kill
            

    