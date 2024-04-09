import numpy as np
import math

print()

def move(change, figures):
    matrix = np.eye(4)
    for i in range(3):
        matrix[i][3] = change[i]
    for i in range(len(figures)):
        for j in range(len(figures[i])):
            point = figures[i][j]
            position = [[point[0]],[point[1]],[point[2]],[1]]
            moved_point = np.matmul(matrix, position)
            figures[i][j] = [moved_point[0][0],moved_point[1][0],moved_point[2][0]]
    return figures

def rotation(change, figures):

    matrix_x = np.eye(4)
    matrix_x[1][1] = math.cos(change[0])
    matrix_x[1][2] = math.sin(change[0])
    matrix_x[2][1] = -math.sin(change[0])
    matrix_x[2][2] = math.cos(change[0])

    matrix_y = np.eye(4)
    matrix_y[0][0] = math.cos(change[1])
    matrix_y[0][2] = -math.sin(change[1])
    matrix_y[2][0] = math.sin(change[1])
    matrix_y[2][2] = math.cos(change[1])

    matrix_z = np.eye(4)
    matrix_z[0][0] = math.cos(change[2])
    matrix_z[0][1] = -math.sin(change[2])
    matrix_z[1][0] = math.sin(change[2])
    matrix_z[1][1] = math.cos(change[2])

    for i in range(len(figures)):
        for j in range(len(figures[i])):
            point = figures[i][j]
            moved_point = [[point[0]],[point[1]],[point[2]],[1]]
            if change[0] != 0:
                moved_point = np.matmul(matrix_x, moved_point)
            if change[1] != 0:
                moved_point = np.matmul(matrix_y, moved_point)
            if change[2] != 0:
                moved_point = np.matmul(matrix_z, moved_point)
            figures[i][j] = [moved_point[0][0],moved_point[1][0],moved_point[2][0]]
    return figures