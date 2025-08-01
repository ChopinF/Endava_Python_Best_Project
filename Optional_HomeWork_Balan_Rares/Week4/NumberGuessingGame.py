secretNumber = 7
number = 0
guesses = 0
while(number != secretNumber and guesses < 3):
    number = int(input("Try to guess the number: "))
    guesses += 1
    if number == secretNumber:
        print("You guessed it!")
        break
    else:
        print("Guess again!")
else:
    print("You did not guess in time")