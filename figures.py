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

    points5 = []
    # x, y, z
    points5.append((100, -500,700))
    points5.append((500, -500,700))
    points5.append((250, -500,400))

    points6 = []
    # x, y, z
    points6.append((100, -500,700))
    points6.append((500, -500,700))
    points6.append((250, -1000,200))

    points7 = []
    # x, y, z
    points7.append((100, -500,700))
    points7.append((250, -500,400))
    points7.append((250, -1000,200))

    points8 = []
    # x, y, z
    points8.append((500, -500,700))
    points8.append((250, -500,400))
    points8.append((250, -1000,200))

    figure = []

    figure.append(points)
    figure.append(points2)
    figure.append(points3)
    figure.append(points4)
    figure.append(points5)
    figure.append(points6)
    figure.append(points7)
    figure.append(points8)

    return figure
