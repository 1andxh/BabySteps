# check if a number is odd or even

print('=' * 40)
print('THE PROGRAM WILL RUN TILL THE USER QUITS \nONLY THEN WILL THE SORTED NUMBERS BE DISPLAYED TO THE USER')
even = []
odd = []

def is_even(number):
    return number % 2 == 0        

def is_odd(number):
    return number % 2 != 0

while True:
    try:
        number = int(input('Enter number (or press q to quit): '))
        if is_even(number):
            even.append(number)
        elif is_odd(number):
            odd.append(number)

    except ValueError:
        break

even.sort()
odd.sort()

print(f'sorted even numbers: {even}')
print(f'sorted odd numbers: {odd}')