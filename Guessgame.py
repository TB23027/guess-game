import random
number_to_guess = random.randint(1,100)
guesses = 0
guesses_1 = 0
guessed = []
while True:
    try:
        guess_1 = int(input("Guess a number between 1 and 100: "))
        if guess_1 in guessed:
            print("Duplicate, try again")

        elif guess_1 > number_to_guess and guess_1 < 101:
            print("Too high!")
            guesses += 1 
            guessed.append(guess_1)
            print(guessed)

        elif guess_1 < number_to_guess and guess_1 > 0:
            guesses += 1
            guessed.append(guess_1)
            print("Too low")
            print(guessed)

        elif guess_1 == number_to_guess:
            guesses += 1
            break
        
        else:
            print("Must be between 1 and 100 please!")
            guesses_1 += 1
        

    except ValueError:
        print("Enter a valid number!")
        guesses_1 += 1

print("Correct!")
print(guessed)
print(f"Number of valid guesses: {guesses}")
print(f"Number of invalid guesses: {guesses_1}")