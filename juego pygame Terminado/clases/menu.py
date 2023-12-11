import pygame

class Menu():
    def __init__(self, x, y, dimx, dimy, path) -> None:
       self.imagen = pygame.image.load(path)
       self.fondo = pygame.transform.scale(self.imagen, (dimx, dimy))
       self.posicion_x = x
       self.posicion_y = y

       
    def mostrar_menu(self, screen:pygame.Surface):
        screen.blit(self.fondo, (self.posicion_x, self.posicion_y))
