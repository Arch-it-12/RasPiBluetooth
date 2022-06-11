import math


def midpoint(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    x = (x1 + x2) / 2
    y = (y1 + y2) / 2

    return int(x), int(y)


def pyth(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def dot(p1, p2, origin):
    x1, y1 = p1
    x2, y2 = p2
    ox, oy = origin

    x1, y1 = ox - x1, oy - y1
    x2, y2 = x2 - ox, y2 - oy

    return (x1 * x2) + (y1 * y2)


def rect(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    return (min(x1, x2, x3, x4), min(y1, y2, y3, y4)), (max(x1, x2, x3, x4), max(y1, y2, y3, y4))


def points(c):
    (ptA, ptB, ptC, ptD) = c.reshape((4, 2))

    ptB = (int(ptB[0]), int(ptB[1]))
    ptC = (int(ptC[0]), int(ptC[1]))
    ptD = (int(ptD[0]), int(ptD[1]))
    ptA = (int(ptA[0]), int(ptA[1]))

    return ptA, ptB, ptC, ptD


def center(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
                (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
                (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

    return int(x), int(y)
