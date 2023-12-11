import pygame

class Rectangulo:
    def __init__(self, x, y, dim_x, dim_y, color):
        self.Rect = pygame.Rect(x, y, dim_x, dim_y)
        self.surface = pygame.Surface((dim_x, dim_y))
        self.surface.fill(color)
        self.posicion_x = x
        self.posicion_y = y
        self.dimencion_x = dim_x
        self.dimencion_y = dim_y

        self.aux_x = x 

    def modificar_posicion_rect(self, posicion_x = 0):
        self.Rect = pygame.Rect(self.posicion_x + posicion_x, self.posicion_y, self.dimencion_x, self.dimencion_y)


    def dibujar(self, screen:pygame.Surface, posicion_x = 0):
        screen.blit(self.surface, (self.posicion_x + posicion_x, self.posicion_y))
