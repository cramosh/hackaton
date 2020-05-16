import pygame, random

screen_width = 1280
screen_height = 960
speed=0
speed_bola_x = 3
speed_bola_y = 3
 #colors
gray_color = (200,200,200)
light_gray = pygame.Color('grey12')

#Conectamos las libreria e iniciamos
pygame.init()
#El reloj indica donde se ejecuta cada frame
clock = pygame.time.Clock()

screen =  pygame.display.set_mode((screen_width,screen_height))

def mover_rectangulo():
    global speed
    rectangulo.top += speed
    if rectangulo.top + 50 > screen_height:
        rectangulo.top = 0 

def mover_bola():
    global speed_bola_x,speed_bola_y

    if bola.top == 0 or bola.top + 50 > screen_height:
        speed_bola_y = -speed_bola_y
    
    if bola.left + 50 > screen_width:
        bola.top = screen_height // 2
        bola.left = screen_width // 2
          
    bola.top += speed_bola_y
    bola.left += speed_bola_x
# Dibujamos los elementos en pantalla
rectangulo = pygame.Rect(10,10,10,140)
bola = pygame.Rect(50,10,50,50)

#Genera un bucle infinito
while True:
    screen.fill(light_gray)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed = -3            
            elif event.key == pygame.K_DOWN:
                speed = 3
        elif event.type == pygame.KEYUP:
            speed = 0

    pygame.draw.rect(screen, gray_color, rectangulo)
    pygame.draw.ellipse(screen, gray_color, bola)
    #Se calculan los graficos y se muestran por pantalla
    pygame.display.flip()

    mover_rectangulo()  
    mover_bola()  
    #Calcula el tiempo entre clicks para indicar la ejecucion por seg
    clock.tick(60)
    pass