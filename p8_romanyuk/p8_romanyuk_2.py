print("Quadratic equation is ax^2+bx+c=0")
try:
    a = float(input("Enter the coeficient a:"))
    b = float(input("Enter the coeficient b:"))
    c = float(input("Enter the coeficient c:"))
    from math import *
    D = b**2-4*a*c
    if D < 0:
        raise Exception("Discriminant less than 0. The equation has no real roots.")
    x1 = (-b + sqrt(D))/(2*a)
    x2 = (-b - sqrt(D))/(2*a)
    if x1 == x2:
        print("There is one root in your equation: x = {}".format(round(x1, 2)))
    else:
        print("The first root: x1 = {} , the secod root: x2 = {}".format(round(x1, 2), round(x2, 2)))
except Exception as e:
    print(e)