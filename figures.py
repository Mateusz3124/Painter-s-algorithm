def createFigures():
    # data
    points = []
    # x, y, z
    points.append((-50, 300,400))
    points.append((400, 300,400))
    points.append((500, 700,400))
    points.append((100,700,400))

    points2 = []
    # x, y, z
    points2.append((-600, 800,100))
    points2.append((-1000, 800,100))
    points2.append((-1000, 1200,700))
    points2.append((-600,1200,700))

    points3 = []
    # x, y, z
    points3.append((-600, 300,700))
    points3.append((-1000, 300,700))
    points3.append((-1000, 900,400))
    points3.append((-600,900,400))

    points4 = []
    # x, y, z
    points4.append((100, 300,700))
    points4.append((500, 300,700))
    points4.append((400, 1200,300))
    points4.append((100,1200,300))

    figure = []

    figure.append(points)
    figure.append(points2)
    figure.append(points3)
    figure.append(points4)
    return figure
