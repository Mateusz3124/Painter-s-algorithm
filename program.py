import pygame
import sys
import math
from figures import createFigures
from translation import move, rotation

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3d models")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up game loop
running = True
start_point = (0, 0)
end_point = (0, 0)

d = 200

order = [[0,1], [0,2], [0,4], [1,3], [1,5], [2,3], [2,6], [3,7], [4,5], [4,6], [7,6], [7,5]]

def map(value):
    x = (value[0] * d)/ value[2] + WIDTH / 2 
    y = HEIGHT / 2 - (value[1] * d)/ value[2]
    return (x,y)

def drawFigure(pointsToDraw):
    for el in order:
        start = pointsToDraw[el[0]]
        end = pointsToDraw[el[1]]
        if start[2] < 0 or end[2] < 0:
            continue
        pygame.draw.line(screen, WHITE, map(start), map(end), 2)
figure = createFigures()
mouse_start_pos = None
figure = move((0,0,2000), figure)
while running:
    move_matrix = [0,0,0]
    rotation_matrix = [0,0,0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_start_pos:
                    mouse_start_pos = None
                else:
                    mouse_start_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEWHEEL:
            d += event.y * 5
            if d < 80:
                d = 80
        if event.type == pygame.MOUSEMOTION:
            if mouse_start_pos:
                mouse_current_pos = pygame.mouse.get_pos()
                mouse_offset_x = mouse_current_pos[0] - mouse_start_pos[0]
                rotation_matrix[1] += mouse_offset_x * 0.01
                mouse_offset_y = mouse_current_pos[1] - mouse_start_pos[1]
                rotation_matrix[0] += mouse_offset_y * 0.01
                mouse_start_pos = mouse_current_pos
                mouse_current_pos = pygame.mouse.get_pos()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_n]:
            rotation_matrix[0] -= 0.01
        if pressed[pygame.K_m]:
            rotation_matrix[0] += 0.01
        if pressed[pygame.K_j]:
            rotation_matrix[1] -= 0.01
        if pressed[pygame.K_l]:
            rotation_matrix[1] += 0.01
        if pressed[pygame.K_u]:
            rotation_matrix[2] -= 0.01
        if pressed[pygame.K_o]:
            rotation_matrix[2] += 0.01
        if pressed[pygame.K_w]:
            move_matrix[2] -= 15
        if pressed[pygame.K_s]:
            move_matrix[2] += 15
        if pressed[pygame.K_z]:
            move_matrix[1] -= 15
        if pressed[pygame.K_x]:
            move_matrix[1] += 15
        if pressed[pygame.K_d]:
            move_matrix[0] -= 15
        if pressed[pygame.K_a]:
            move_matrix[0] += 15
        if pressed[pygame.K_k]:
            d -= 5
            if d < 80:
                d = 80
        if pressed[pygame.K_i]:
            d += 5
    screen.fill((0, 0, 0))
    if not (move_matrix[0] == 0 and move_matrix[1] == 0 and move_matrix == 0):
        figure = move(move_matrix,figure)
    figure = rotation(rotation_matrix, figure)
    for current_points in figure:
        drawFigure(current_points)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
