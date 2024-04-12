
import sys
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
    if border_two[0][0] <= border_one[0][0] <= border_two[0][1]:
        if border_two[1][0] <= border_one[1][0] <= border_two[1][1] or border_two[1][0] <= border_one[1][1] <= border_two[1][1]:
            return True
    if border_two[0][0] <= border_one[0][1] <= border_two[0][1]:
        if border_two[1][0] <= border_one[1][0] <= border_two[1][1] or border_two[1][0] <= border_one[1][1] <= border_two[1][1]:
            return True
    return False    

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
    border_one = findBorder(figure_one)
    border_two = findBorder(figure_two)
    if not containts_border(border_one, border_two):
        return False
    cond = True
    mapped_one = []
    for i in figure_one:
        if(i[2] < 0):
            cond = False
            break
        mapped_one.append(map(i))
    mapped_two = []
    for i in figure_two:
        if(i[2] < 0):
            cond = False
            break
    if cond:
        mapped_two.append(map(i))
        border_one = findBorder(mapped_one)
        border_two = findBorder(mapped_two)
        if not containts_border(border_one, border_two):
            return False
    plane_one = calc_plane(figure_one[0],figure_one[1],figure_one[2])
    plane_two = calc_plane(figure_two[0],figure_two[1],figure_two[2])
    value_one_camera = calc_value(plane_one, [0,0,0])
    value_two_camera = calc_value(plane_two, [0,0,0])
    cond_test_3 = True
    for el in figure_one:
        if value_two_camera * calc_value(plane_two,el) > 0:
            cond_test_3 = False
    if cond_test_3:
        return False
    cond_test_4 = True
    for el in figure_two:
        if value_one_camera * calc_value(plane_one,el) < 0:
            cond_test_4 = False
    if cond_test_4:
        return False
    return True
WIDTH, HEIGHT = 800, 800
d = 400
def map(value):
    x = (value[0] * d)/ value[2] + WIDTH / 2 
    y = HEIGHT / 2 - (value[1] * d)/ value[2]
    return (x,y)

figure_one = []
figure_two = []

figure_one.append([100,100,100])
figure_one.append([100,200,100])
figure_one.append([150,100,200])
figure_one.append([150,200,200])


figure_two.append([110,100,150])
figure_two.append([110,200,150])
figure_two.append([50,100,170])
figure_two.append([50,200,180])

print(handle_depth_overlapping(figure_one, figure_two))