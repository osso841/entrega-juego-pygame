import random
from clases.imagen import Imagen
from clases.menu import Menu
from clases.opciones import Opciones
from clases.personaje import Personaje
from clases.rectangulo import Rectangulo
from clases.scoreDB import ScoreDB
from pygame.locals import K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_SPACE
import pygame

pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode([1280, 720])
font = pygame.font.SysFont("Arial", 40)
font_usuario = pygame.font.SysFont("Arial Sparrow", 70)


lista_key = [K_0, K_1, K_2, K_3, K_4,K_5,K_6,K_7,K_8, K_9, K_SPACE]

ingresar_menu_tiempo = False
ingresar_menu_escape = False

TIEMPO_JUEGO = 30
segundos = TIEMPO_JUEGO
vidas = 5
contador_errores = 0
palabras_correctas = 0
x_mapa = 0
ingreso = ''
posicion_derecha = True 

saltar = False


#lista palabras random combate
palabras_4_5_letras = [
    'pied', 'hoja', 'taza', 'cafe', 'gato', 'casa', 'luz', 'sol', 'flor', 'mesa',
    'paso', 'vino', 'lago', 'olla', 'faro', 'rio', 'ruin', 'foca', 'vino',
    'piel', 'hora', 'luna', 'pato', 'fino', 'pino', 'sala', 'cola',
    'risa', 'pura', 'cine', 'pila', 'puma', 'cien', 'red'
]

palabras_6_7_letras = [
    'piedra', 'ventil', 'cadena', 'murmul', 'sabana', 'escala', 'cuerda', 'mueble', 'barco', 'cambio',
    'rayo', 'techo', 'florar', 'planta', 'calle', 'barro', 'risita', 'paloma', 'diario',
    'fiesta', 'ventil', 'jirafa', 'bruja', 'granja', 'camino', 'radio', 'rincon', 'vaso', 'acero',
    'carcel', 'camino', 'flauta', 'roble', 'diente', 'bravo', 'cinta', 'velero', 'estilo', 'piedra',
    'tobillo', 'nieve', 'cima', 'ciudad'
]

palabras_7_8_letras = [
    'guitar', 'arroyo', 'amazing', 'sardina', 'freedom', 'jardin', 'veloz', 'lapiz', 'fantasy', 'mariposa',
    'concept', 'brillar', 'quality', 'sensual', 'kitchen', 'consulta', 'maximum', 'musical', 'science', 'ilusion',
    'balance', 'biggest', 'cerdo', 'captain', 'tiempo', 'enjoyed', 'parallel', 'almohada', 'whisper', 'carreta',
    'fortuna', 'neutron', 'premium', 'pajaro', 'relaxing', 'noodles', 'zoologico', 'justice', 'peluche', 'diamond'
]

palabras_4_5_letras_sin_tilde = palabras_4_5_letras.copy()
palabras_6_7_letras_sin_tilde = palabras_6_7_letras.copy()
palabras_7_8_letras_sin_tilde = palabras_7_8_letras.copy()

palabra = random.choice(palabras_4_5_letras_sin_tilde).lower()
borrar_palabra = palabras_4_5_letras_sin_tilde.remove(palabra)

tiempo_incremento_velocidad_enemigo = 0
cambio_posicion_derecha = True
cambio_posicion_izquierda = True


#variables personaje - enemigo
primer_contacto = True

#variables saltos
contador_salto = 10

#OBJETOSS ACTUALES
personaje = Personaje(640, 530, 40, 100, (255, 0, 0),'imagenes\\personaje izquierda.png', 6, 750, 150)
enemigo  = Personaje(1100, 530, 40, 100, (255, 255, 0),'imagenes\\movimiento_enemigo_izquierda1.png', 11, 1650, 176)
mapa_derecha = Rectangulo(640, 0, 800, 720, (0, 255, 255))
mapa_izquierda = Rectangulo(-160, 0, 800, 720, (0, 255, 0))
pantalla = Rectangulo(0, 0, 1280, 720, (0,0,0))

#superficies
bosque_fondo = Imagen('imagenes\\bosque.jpg', 0, 0, 1280, 720)
Etiqueta_tiempo = Imagen('imagenes\\tiempo restante.png', 20, 62, 264, 46) #
etiqueta_incorrectas = Imagen('imagenes\\errores.png', 950, 120, 130, 50) #
etiqueta_palabras_correctas = Imagen('imagenes\\palabras.png', 950, 60, 160, 120) #
etiqueta_recuadro = Imagen('imagenes\\recuadro1.png', 440, 80, 400, 80) #

vidas_juego = Imagen("imagenes\\vidas.png", 50, 620, 100, 100)
posicion_vida = vidas_juego.posicion_x

#TEMPORIZADOR
temporizador_segundos = pygame.USEREVENT
pygame.time.set_timer(temporizador_segundos, 1000)


# variables MENU
mi_menu = Menu(0, 0, 1280, 720, "fondo\\pantalla-comienzo-demon-slayer.jpg")
menu_score = Menu(0, 0, 1280, 720, "fondo\\registros_score.jpg")
menu_ingresar_usuario = Menu(0, 0, 1280, 720, "fondo\\fondo-agregar-usuario.png")

boton_configuracion = Opciones(525, 350, "botones primarios\\btn_configuracion.png")
boton_comenzar = Opciones(525, 450, "botones primarios\\btn_comenzar_partida.png")
boton_registro = Opciones(525, 550, "botones primarios\\registro.png")
boton_volver = Opciones(525, 650, "botones primarios\\btn_volver.png")

puntuacion_base_datos = ScoreDB()
puntuacion_base_datos.crear_DB()


entrar_score = False
ingreso_base_datos = True
lista_scores = []
ingreso_menu_usuario = False
ingreso_nombre_usuario = 'Player'

comenzar_juego = False #!IMPORTANTE

#SONIDOS
sonido_golpe_personaje = pygame.mixer.Sound("sonidos\\sonido-golpe-personaje.mp3")
sonido_golpe_enemigo = pygame.mixer.Sound("sonidos\\sonido-golpe_enemigo.mp3")
sonido_fondo = pygame.mixer.Sound("sonidos\\sonido fondo.mp3")
sonido_click_usuario = pygame.mixer.Sound("sonidos\\sonido-tecla-usuario.mp3")
sonido_click_menu = pygame.mixer.Sound("sonidos\\sonido-click-menu.mp3")
sonido_vida = pygame.mixer.Sound("sonidos\\vida.mp3")

sonido_fondo.set_volume(0.02)
sonido_golpe_enemigo.set_volume(0.3)
sonido_golpe_personaje.set_volume(0.3)
sonido_click_usuario.set_volume(0.3)
sonido_click_menu.set_volume(0.3)
sonido_vida.set_volume(0.3)
sonido_fondo.play(-1)


#CORRECIONES JUGABILIDAD
primera_etapa = True
segunda_etapa = True

#RANDOM DE AVANCE
tiempo_random = random.randint(4, 9)

