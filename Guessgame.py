import random
number_to_guess = random.randint(1,100)
guesses = 0
guessed = []
while True:
    try:
        guess_1 = int(input("Guess a number between 1 and 100: "))
        if guess_1 in guessed:
            print("Duplicate, try again")

        elif guess_1 > number_to_guess and guess_1 < 101:
            print("Too high!")
            guesses += 1 

        elif guess_1 < number_to_guess and guess_1 > 0:
            guesses += 1
            guessed.append(guess_1)
            print("Too low")

        elif guess_1 == number_to_guess:
            guesses += 1
            break
        
        else:
            print("Must be between 1 and 100 please!")
            guesses += 1
        

    except ValueError:
        print("Enter a valid number!")

print("Correct!")
print(f"Number of guesses: {guesses}")