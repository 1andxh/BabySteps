import math
# prompt user 

print('Temperature conversion')
print('=' * 20)
print('1.celsius to fahrenheit \n2.fahrenheit to celsius')
def celsius_to_fahrenheit():
    celsius = float(input('enter the temperature in Celsius: '))
    if not math.isnan(celsius):
        fahrenheit = (celsius * 9) / 5 + 32
        print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees fahrenheit")
    else:
        print('enter a valid number for the temperature in celsius')


def fahrenheit_to_celsius():
    fahrenheit = float(input('enter temperature in fahrenheit'))
    if not math.isnan(fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        print(f'{fahrenheit} degrees fahrenheit is the same as {celsius} degree celsius')
    else:
        print('enter valid number')

while True:
    
    choice = str(input("choose conversion (press q to quit): "))

    if choice == "1":
        celsius_to_fahrenheit()
    elif choice == '2':
        fahrenheit_to_celsius()
    elif choice == 'q':
        break
    else:
        print('Invalid input! Enter number')