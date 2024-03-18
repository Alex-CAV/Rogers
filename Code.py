from PIL import Image
import numpy as np


def bresenham(x1, y1, x2, y2, image):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if x1 < x2:
        sx = 1  
    else: 
        sx = -1

    if y1 < y2:
       sy = 1 
    else:
       sy = -1

    x, y = x1, y1

    epsilon = dx - dy

    while True:
        image.putpixel((x,y),(255, 255, 255))
        if x == x2 and y == y2:
            break
        e2 = 2 * epsilon
        if e2 > -dy:
            epsilon -= dy
            x += sx
        if e2 < dx:
            epsilon += dx
            y += sy
    image.show()

def roggers_clipper(obj_file, image : Image):

    def is_plane_visible(pl : list):
        global dots
        global center

        a = np.array([dots[pl[0]][0] - center[0], dots[pl[0]][1] - center[1], dots[pl[0]][2] - center[2]])
        b = np.array([0, 0, -1])

        if (a.dot(b) <= 0):
            return False
        else:
            return True

    dots = []
    center = [0,0,0]
    plane = []

    with open(obj_file) as file:
        info = file.read().split('\n')

    for line in info:
        if (line.find("v") == 0):
            _, *line = line.split()
            dots.append( list(float(dot) for dot in line) )
        elif (line.find("f") == 0):
            _, *line = line.split()
            plane.append( list(int(fig) for fig in line) )


    for i in range(len(dots)):
        center[0] += dots[i][0]
        center[1] += dots[i][1]
        center[2] += dots[i][2]
    center[0] /= len(dots)
    center[1] /= len(dots)
    center[2] /= len(dots)


    for i in range(len(plane)):
        pl = plane[i]
        if (is_plane_visible(pl)):
            for i in range(len(pl) + 1):
                bresenham(((int(dots[pl[i]][0]), int(dots[pl[i]][1])), (int(dots[pl[i+1]][0]), int(dots[pl[i+1]][1]))), image)
