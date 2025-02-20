guess_word = "coke"
player_guess = ""
guess_limit = 3
guess_count = 0

player = input("Enter your name: ")
print(f'\nWelcome, {player.upper()}! Take a guess.')

while player_guess.casefold() != guess_word and guess_count < guess_limit:
    if guess_count == 0:
        print("\nClue 1: World's most popular drink.")
    
    elif guess_count == 1:
        print("\nClue 2: It’s a fizzy soft drink.")

    elif guess_count == 2:
        print("\nClue 3: Its main rival is Pepsi.")

    # Get player input
    player_guess = input(">> ")
    
    # Increase guess count and decrease guess limit
    guess_count += 1
    # guess_limit -= 1

    # Check if the guess is correct
    if player_guess.casefold() == guess_word:
        print("\nCongrats! You won!!! 🎉")
        break 

# If out of guesses
if player_guess.casefold() != guess_word:
        print("\nOops! You have used all your guesses. The correct word was:", guess_word.upper())
