l=int(input("enter length:"))
b=int(input("enter breadth:"))
h=int(input("enter height:"))
x = lambda a: a * a
print("area of square is ",(x(1)))
y = lambda a, b : a*b
print("area of rectangle is ",(y(1,b)))
z = lambda a, b : 1/2 * (a*b)
print("area of triangle is ",(z(b,h)))