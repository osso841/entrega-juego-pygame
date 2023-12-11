import pygame

class Imagen:
    def __init__(self, path, x, y, scale_x, scale_y):
        self.fondo = pygame.image.load(path)
        self.fondo_escala = pygame.transform.scale(self.fondo, (scale_x, scale_y))
        self.dimension_x = scale_x
        self.posicion_x = x
        self.posicion_y = y


    def dibujar(self, screen:pygame.Surface, posicion_x = None):
        if posicion_x is None:
            screen.blit(self.fondo_escala, (self.posicion_x, self.posicion_y))
        else:
            screen.blit(self.fondo_escala, (posicion_x, self.posicion_y))
