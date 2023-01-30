import math

class circle:
    def __init__(sl, x, y, r ):
        sl.X=x
        sl.Y=y
        sl.R=r
    def area(sl):
        return math.pi*sl.r*sl.r
    