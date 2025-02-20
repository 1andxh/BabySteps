# to find the area of a /\
# area = 1/2 * base * height

def area_of_triangle():
    base = float(input('base: '))
    height = float(input("height: "))

    area = 0.5 * base * height
    print(area)
    if base <= 0 or height <= 0:
        print("enter valid number")
    else:
        return area
    
area_of_triangle()
    
