def get_sum():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))   
    try:
        result = num1 + num2        
    except ValueError:
        print("please enter a number")
    else:
        print(result)

            
get_sum()


