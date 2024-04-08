def createFigures():
    # data
    points = []
    # x, y, z
    points.append((100, 300,400))
    points.append((500, 300,400))
    points.append((100, 300,650))
    points.append((500, 300,650))

    points.append((100,1000,400))
    points.append((500, 1000,400))
    points.append((100, 1000,650))
    points.append((500,1000,650))

    points2 = []
    # x, y, z
    points2.append((-100, 300,400))
    points2.append((-500, 300,400))
    points2.append((-100, 300,650))
    points2.append((-500, 300,650))

    points2.append((-100,1000,400))
    points2.append((-500, 1000,400))
    points2.append((-100, 1000,650))
    points2.append((-500,1000,650))

    points3 = []
    # x, y, z
    points3.append((-100, 300,700))
    points3.append((-500, 300,700))
    points3.append((-100, 300,950))
    points3.append((-500, 300,950))

    points3.append((-100,1000,700))
    points3.append((-500, 1000,700))
    points3.append((-100, 1000,950))
    points3.append((-500,1000,950))

    points4 = []
    # x, y, z
    points4.append((100, 300,700))
    points4.append((500, 300,700))
    points4.append((100, 300,950))
    points4.append((500, 300,950))

    points4.append((100,1000,700))
    points4.append((500, 1000,700))
    points4.append((100, 1000,950))
    points4.append((500,1000,950))

    figure = []

    figure.append(points)
    figure.append(points2)
    figure.append(points3)
    figure.append(points4)
    return figure
