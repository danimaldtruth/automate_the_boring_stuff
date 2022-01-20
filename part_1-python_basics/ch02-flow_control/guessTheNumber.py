# This is a guess the number game
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break #this condition is the correct guess

if guess == secretNumber:
    print('Good Job! You guessed my number in ' +str(guessesTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(SecretNumber)')


#note for python group. how to easily rename python files in pycharm so guessTheNumber.py can become guess_the_number.py for pythong convention.
# additional note, what am i doing wrong here that prevents this to execute correctly