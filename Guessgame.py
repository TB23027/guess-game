import random
number_to_guess = random.randint(1,100)
guesses = 0
while True:
    try:
        guess_1 = int(input("Guess a number between 1 and 100: "))
        if guess_1 == number_to_guess:
            guesses += 1
            break
        elif guess_1 > number_to_guess:
            print("Too high!")
            guesses += 1 
        else:
            print("Too low")
            guesses += 1
    except ValueError:
        print("Try again: ")

print("Correct!")
print(f"Number of guesses: {guesses}")