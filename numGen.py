import random
min_range = int(input('enter the minimum value of the range: '))
max_range = int(input('enter the maximum value of the range: '))
try: 
    if min_range <= max_range:
        random_num = random.uniform(min_range, max_range)
        print(f"A random numer between {min_range} and {max_range} is: {random_num}")
except ValueError:
        print('Please enter valid numbers, ensuring that the minimun value is less than the maximum value.')