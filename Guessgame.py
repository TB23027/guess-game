import random
# This imports random (a list of code written by someone else)
# so that we can pick a random number between 1,100 each time.

number_to_guess = random.randint(1,100)
guesses = 0
guesses_1 = 0
guessed = []
# These variables are the base numbers so they will 
# be added to throughout the code so that the next time 
# we run the code they will reset back to 0.
while True: 
# This is the beginning of the while loop meaning everything 
# within this loop will be repeated until the user enters 
# the correct answer which will "break" the code.
    try:
        guess_1 = int(input("Guess a number between 1 and 100: "))
        if guess_1 in guessed:
            print("Duplicate, try again")
            guesses_1 += 1
# If a user enters the same number more than once,
# this message will be displayed.
# This guess will be added to a running total of 
# invalid guesses which will be displayed at the end.

        elif guess_1 > number_to_guess and guess_1 < 101:
            print("Too high!")
            guesses += 1 
            guessed.append(guess_1)
            print(guessed)
# When a user inputs a number that is below 101 
# and above the number to guess,
# the words "Too high" will be displayed.
# This then adds there guess to a
# list and displays it after each turn,
# and a running total of guesses will be added
# to after the user inputs it.

        elif guess_1 < number_to_guess and guess_1 > 0:
            guesses += 1
            guessed.append(guess_1)
            print("Too low")
            print(guessed)
# If a user enters a number below the number to guess and above 0,
# the message "Too low" will be displayed. 
# This also adds the guess to the list and and 
# prints the updated guessed list. 
# This then adds 1 to the running total of valid guesses.
        elif guess_1 == number_to_guess:
            guesses += 1
            break
# When a user guesses the random number, 
# this will break the while loop and skip any other elif or elses.
        
        else:
            print("Must be between 1 and 100 please!")
            guesses_1 += 1
# If a user enters a number above 100 and below 1,
# this will prompt them to re-enter it and 
# also add it to invalid guesses.

    except ValueError:
        print("Enter a valid number!")
        guesses_1 += 1
# When someone enters something that is not a number,
# so something like a letter, it will say enter a valid number
# and then add another guess to the invalid guess total.

print("Correct!")
print(guessed)
print(f"Number of valid guesses: {guesses}")
print(f"Number of invalid guesses: {guesses_1}")
# This starts as soon as the while loop is broken
# and they guess the right answer.
# The user will see the word "correct!" printed
# and then the list of guesses as well as invalid and valid guesses