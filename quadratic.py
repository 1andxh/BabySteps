# solve quadratic equations
import math

# coefficients
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# discriminants
discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant))/(2*a)
    