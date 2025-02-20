import math
# check if a number is positive, negative or zero

def num_checker():
    while True:
        try: 
            number = int(input("enter a number: "))
        
            if number > 0 :
                print(f'{number} is a positive number')
            elif number < 0:
                print(f'{number} is a negative number')
            else:
                print(f'you have entered zero')
        except ValueError:
                    print("Enter a valid number!")
                    break

num_checker()
