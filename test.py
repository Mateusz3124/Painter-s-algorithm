d = 5

points = []
points.append((100, 300,40))
points.append((400, 300,40))
points.append((200, 300,50))
points.append((600, 300,50))

points.append((100,1000,40))
points.append((400, 1000,40))
points.append((200, 1000,50))
points.append((600,1000,50))

points2d = []

for point in points:
    x = (point[0] * d)/ point[2]
    y = (point[1] * d)/ point[2]
    points2d.append((x,y))
for el in points2d:
    print(el)
order = [[0,1], [0,2], [0,4], [1,3], [1,5], [2,3], [2,6],  [4,5], [4,6], [7,6], [7,5]]
for el in order:
    print(str(points2d[el[0]]) + " " + str(points2d[el[1]]))