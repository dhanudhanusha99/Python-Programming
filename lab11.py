import graphics.rectangle
print("Rectangle")
l=int(input("Enter the length : "))
b=int(input("Enter the breadth : "))
print("Area : ",graphics.rectangle.area(l,b))
print("Perimeter : ",graphics.rectangle.perimeter(l,b))

from graphics.circle import area as a
from graphics.circle import perimeter as p
print("Circle")
r=int(input("Enter the radius : "))
print("Area : ",a(r))
print("Perimeter : ",p(r))

from graphics.dgraphics.cuboid import area as a
from graphics.dgraphics.cuboid import perimeter as p
print("Cuboid")
l=int(input("Enter the length : "))
b=int(input("Enter the breadth : "))
h=int(input("Enter the height : "))
print("Area : ",a(l,b,h))
print("Perimeter : ",p(l,b,h))

from graphics.dgraphics.sphere import *
print("Sphere")
r=int(input("Enter the radius : "))
print("Area : ",area(r))
print("Circumference : ",circumference(r))


