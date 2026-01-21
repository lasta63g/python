import random


def play_guessing_game():
    levels=int(input("CHOOSE LEVEL from 1-3"))
    while levels not in [1, 2, 3]:
        print("Invalid level! Choose 1, 2, or 3.")
        levels = int(input("CHOOSE LEVEL from 1-3: "))
    if levels == 1:
        secret_number = random.randint(1, 10)
        print("Easy Level (1-10)")
    elif levels == 2:
        secret_number = random.randint(1, 50)
        print("Medium Level (1-50)")
    else:
        secret_number = random.randint(1, 100)
        print("Hard Level (1-100)")
        
    Guess=None
    attempts=0
    max_attempts=5

    while Guess!= secret_number and attempts<max_attempts:
        Guess=int(input("Enter your guess"))
        attempts += 1            
        if(Guess > secret_number ):
            print("Your guess is High!")
        elif(Guess < secret_number ):
            print("You guess is low!")
        else:
            print("You did it!!!")
            print("You did it in",attempts,"attempts")
    if Guess != secret_number:
        print("game over")
play_again='y'
while play_again =='y':
    play_guessing_game()
    play_again=input("Play Again y/n?:")

