from packages.graphics.graphics3D import cuboid
from packages.graphics.circle_area import *
import packages.graphics.rect
l = 10
b = 20
w = 5
r = 2
print("Area of rectangle: ",packages.graphics.rect.getArea(l,b))
print("area of cuboid : ",cuboid.getArea(l,b,w))
print("area of circle: ",circle_area(r))
