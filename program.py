import pygame
import sys
import math
import random
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

d = 400

def findBorder(figure):
    x = [sys.maxsize, -sys.maxsize]
    y = [sys.maxsize, -sys.maxsize]
    for i in figure:
        x[0] = min(x[0], i[0])
        x[1] = max(x[1], i[0])
        y[0] = min(y[0], i[1])
        y[1] = max(y[1], i[1])
    return (x,y)

def containts_border(border_one, border_two):
    if border_one[0][0] > border_two[0][1]:
        return False
    if border_one[0][1] < border_two[0][0]:
        return False
    if border_one[1][0] > border_two[1][1]:
        return False
    if border_one[1][1] < border_two[1][0]:
        return False
    return True    

def calc_plane(a, b, c):
    abx = b[0] - a[0]
    aby = b[1] - a[1]
    abz = b[2] - a[2]
    acx = c[0] - a[0]
    acy = c[1] - a[1]
    acz = c[2] - a[2]
    nx = aby * acz - abz * acy
    ny = abz * acx - abx * acz
    nz = abx * acy - aby * acx
    if nx==0 and ny==0 and nz==0:
        return None                
    return (nx, ny, nz, -nx*a[0]-ny*a[1]-nz*a[2])

def calc_value(var, value):
    sum = 0
    for i in range(len(value)):
        sum += value[i] * var[i]
    sum += var[3]
    return sum

def handle_depth_overlapping(figure_one, figure_two):
    if figure_one[1] > figure_two[0]:
        return False
        
    curren_figure_one = figure_one[2]
    current_figure_two = figure_two[2]

    border_one = findBorder(curren_figure_one)
    border_two = findBorder(current_figure_two)
    if not containts_border(border_one, border_two):
        return False
    cond = True
    mapped_one = []
    for i in curren_figure_one:
        if(i[2] < 0):
            cond = False
            break
        mapped_one.append(map(i))
    mapped_two = []
    for i in current_figure_two:
        if(i[2] < 0):
            cond = False
            break
        mapped_two.append(map(i))
    if cond:
        border_one = findBorder(mapped_one)
        border_two = findBorder(mapped_two)
        if not containts_border(border_one, border_two):
            return False
    plane_one = calc_plane(curren_figure_one[0],curren_figure_one[1],curren_figure_one[2])
    plane_two = calc_plane(current_figure_two[0],current_figure_two[1],current_figure_two[2])
    value_one_camera = calc_value(plane_one, [0,0,0])
    value_two_camera = calc_value(plane_two, [0,0,0])
    cond_test_3 = True
    for el in curren_figure_one:
        if -0.001 <= calc_value(plane_two,el) <= 0.001:
            continue
        if value_two_camera * calc_value(plane_two,el) > 0:
            cond_test_3 = False
    if cond_test_3:
        return False
    cond_test_4 = True
    for el in current_figure_two:
        if -0.001 <= calc_value(plane_one,el) <= 0.001:
            continue
        if value_one_camera * calc_value(plane_one,el) < 0:
            cond_test_4 = False
    if cond_test_4:
        return False
    return True

def sortFigure(figure):
    sorted_by_z = []
    for current_figure in figure:
        min_z = min(node[2] for node in current_figure)
        max_z = max(node[2] for node in current_figure)
        cond = True
        for i in range(len(sorted_by_z)):
            if sorted_by_z[i][0] < max_z:
                sorted_by_z.insert(i,[max_z, min_z, current_figure, len(sorted_by_z)])
                cond = False
                break
        if cond:
            sorted_by_z.append([max_z, min_z, current_figure, len(sorted_by_z)])

    result = []
    order = []
    while len(sorted_by_z) != 0:
        for i in range(len(sorted_by_z)):
            cond = True
            for j in range(i + 1, len(sorted_by_z)):
                if i != j:
                    if handle_depth_overlapping(sorted_by_z[i],sorted_by_z[j]):
                        cond = False
            if cond:
                result.append(sorted_by_z[i][2])
                order.append(sorted_by_z[i][3])
                sorted_by_z.remove(sorted_by_z[i])
                break
    return result, order

def fun(sorted_by_z):
    if len(sorted_by_z) <= 1:
        return sorted_by_z
    before = []
    after = []
    for i in range(1, len(sorted_by_z)):
        if handle_depth_overlapping(sorted_by_z[0][2], sorted_by_z[i][2]):
            before.append(sorted_by_z[i])
        else:
            after.append(sorted_by_z[i])
    
    before = fun(before)
    after = fun(after)
    result = []
    for i in before:
        result.append(i)
    result.append(sorted_by_z[0])
    for i in after:
        result.append(i)
    return result

def map(value):
    x = (value[0] * d)/ value[2] + WIDTH / 2 
    y = HEIGHT / 2 - (value[1] * d)/ value[2]
    return (x,y)

def drawFigure(pointsToDraw, color):
    figureToDraw = []
    for i in pointsToDraw:
        if(i[2] < 0):
            return
        figureToDraw.append(map(i))
    pygame.draw.polygon(screen, color, figureToDraw)

figure = createFigures()
color = []
for i in range(len(figure)):
    color.append(pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

mouse_start_pos = None
figure = move((0,0,2500), figure)
start_condition = True
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
            if d < 400:
                d = 400
        if pressed[pygame.K_i]:
            d += 5
    screen.fill((0, 0, 0))
    if not (move_matrix[0] == 0 and move_matrix[1] == 0 and move_matrix[2] == 0) or start_condition:
        figure = move(move_matrix,figure)
    figure = rotation(rotation_matrix, figure)
    if not (move_matrix[0] == 0 and move_matrix[1] == 0 and move_matrix[2] == 0) or not (rotation_matrix[0] == 0 and rotation_matrix[1] == 0 and rotation_matrix[2] == 0) or start_condition:
            figure, order = sortFigure(figure)
            copyColor = []
            for i in order:
                copyColor.append(color[i])
            color = copyColor
    for i in range(len(figure)):
        drawFigure(figure[i], color[i])

    # Update the display
    pygame.display.flip()
    start_condition = True

# Quit Pygame
pygame.quit()
sys.exit()
