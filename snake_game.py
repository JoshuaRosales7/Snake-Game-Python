import pygame
import time
import random

pygame.init()

# Definir colores
white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)
red = (213, 50, 80)

dis_width = 600
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game por [Tu Nombre]')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 25)

def your_score(score):
    value = score_font.render("Puntuación: " + str(score), True, black)
    dis.blit(value, [10, 10])

def draw_snake(snake_block, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(dis, black, [x, y, snake_block, snake_block])

def display_message(msg, color, y_displacement=0, font_size=30):
    mesg = pygame.font.SysFont(None, font_size).render(msg, True, color)
    text_rect = mesg.get_rect(center=(dis_width / 2, dis_height / 2 + y_displacement))
    dis.fill(white)  # Llenar la pantalla de blanco antes de mostrar el mensaje
    dis.blit(mesg, text_rect)
    pygame.display.update()

# Mensaje de bienvenida
display_message("Toca una tecla para iniciar", black, 100, 25)
pygame.display.update()
time.sleep(2)  # Espera 2 segundos antes de comenzar

game_over = False
game_close = False

x1 = dis_width / 2
y1 = dis_height / 2

x1_change = 0
y1_change = 0

snake_list = []
length_of_snake = 1

foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_close = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
    snake_head = [x1, y1]
    snake_list.append(snake_head)
    if len(snake_list) > length_of_snake:
        del snake_list[0]

    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_close = True

    draw_snake(snake_block, snake_list)
    your_score(length_of_snake - 1)

    pygame.display.update()

    if game_close:
        display_message("Has perdido. Presiona Q-Quitar o C-Jugar de nuevo", red, 0, 30)
        pygame.display.update()
        
        # Esperar a que el jugador presione "Q" o "C"
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        waiting_for_input = False
                    elif event.key == pygame.K_c:
                        game_close = False
                        x1 = dis_width / 2
                        y1 = dis_height / 2
                        x1_change = 0
                        y1_change = 0
                        snake_list = []
                        length_of_snake = 1
                        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                        waiting_for_input = False

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        length_of_snake += 1

    clock.tick(snake_speed)

pygame.quit()
quit()
