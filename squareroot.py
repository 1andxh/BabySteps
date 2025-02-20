import math
while True:
    num = int(input("enter a non-negative number: "))
    if num > 0:
        squareOfNum = math.sqrt(num)
        print(f"square root of {num} is: {squareOfNum}")

    else:
        print("you have entered a negative nunber")