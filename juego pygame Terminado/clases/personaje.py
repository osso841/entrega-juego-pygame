import pygame
from funciones import obtener_superficie_desde_spritesheet
from clases.rectangulo import Rectangulo

class Personaje(Rectangulo):
    def __init__(self, x, y , dim_x, dim_y, color, path, columnas, escala_x, escala_y):
        super().__init__(x, y, dim_x, dim_y, color)

        self.caminar = obtener_superficie_desde_spritesheet(path, columnas, escala_x, escala_y)
        self.posicion = 0
        self.animacion = self.caminar
        self.imagen = self.caminar[self.posicion]

    def actualizar(self):
        if self.posicion < len(self.animacion)-1:
            self.posicion += 1
        else:
            self.posicion = 0

        self.imagen = self.animacion[self.posicion]


    def detener_personaje(self, path, escala_x, escala_y):
        self.imagen = pygame.image.load(path)
        self.imagen = pygame.transform.scale(self.imagen, (escala_x, escala_y))


    def cambiar_imagen(self, path, columnas, escala_x, escala_y):
        self.caminar =  obtener_superficie_desde_spritesheet(path, columnas, escala_x, escala_y)
        self.animacion = self.caminar
        self.imagen = self.caminar[self.posicion]

    def mostrar_personaje(self, screen:pygame.Surface, centrar_y = 0, posicion_x=None):
        if posicion_x is None:
            screen.blit(self.imagen, (self.posicion_x - 50, self.posicion_y - 30 -centrar_y))
        else:
            screen.blit(self.imagen, (self.posicion_x + posicion_x - 50, self.posicion_y - 30 - centrar_y))
