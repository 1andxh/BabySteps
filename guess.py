secret_word = "coke"
guess = ""
guess_count = 0
guess_limit = 3
player = input("enter your name: ")

print(f"Welcome! {player.upper()} , this is a guess-game")
print("You have three attempts to guess the secret word.(clues will be provided)\n")

while guess.casefold() != secret_word:
    if guess_count == 0:
        guess_count += 1
        print("\nClue 1: world most popular drink")
        guess = input("enter guess word: ")
        guess_limit -= 1

    elif guess.casefold() != secret_word:
        guess_count += 1
        print("\nclue 2: sponsored world cup ")
        guess = input("enter guess word: ")
        guess_limit -= 1

    elif guess.casefold() != secret_word:
        guess_count += 1
        print("\nClue 3: brrrrrrr!!!: ") 
        guess = input("enter guess word: ")
        guess_limit -= 1

    elif guess_limit == 0:
        print("\noops! Out of guesses!")

else:
    guess == secret_word
    print("yay! you won")

