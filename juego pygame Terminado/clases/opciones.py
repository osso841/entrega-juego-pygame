import pygame

class Opciones():
    def __init__(self, x, y, path) -> None:
        self.imagen = pygame.image.load(path)
        self.rect_boton = pygame.Rect(x, y, self.imagen.get_width() ,self.imagen.get_height())
        self.posicion_x = x
        self.posicion_y = y

    def mostrar_opciones(self, screen:pygame.Surface):
        screen.blit(self.imagen, (self.posicion_x, self.posicion_y))
