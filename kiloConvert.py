# convert km to m
import math
def kilo_convert():
    Kilometers = float(input('Enter the distance in km: '))
    to_mile_factor = 0.621371

    if not math.isnan(Kilometers):
        miles = Kilometers * to_mile_factor
        print(f'{Kilometers} kilometers is approximately {miles} miles.')
    else:
        print('Please enter a vlaid number for the distance in kilometers')

kilo_convert()