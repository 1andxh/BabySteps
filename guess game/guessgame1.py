import random

def get_random_num():
    secret_number = random.randint(1,100)
    attempts = 0
    print("I'm thinking of a number between 1-100")

    while True:
        try:
            print("Take a guess: ")
            
            guess = int(input(">> "))
            attempts += 1

            if guess < secret_number:
                print("Too low! try again")

            elif guess > secret_number:
                print("Too high! try again")

            else:
                print(f'you guessed the {secret_number} in {attempts} attempts')

        except ValueError:
            print("numbers only!")



get_random_num()

