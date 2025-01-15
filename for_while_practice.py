# Step 1: Understand `for` loops.

print("These numbers are even numbers:")

for i in range(1, 11):
    if i % 2 == 0:      # This modulo function inside the `if` statement checks if the numbers are even inside the `for` loop.
        print(i)

print("")

print("These numbers are odd numbers:")

for i in range(1,11):
    if i % 2 == 1:      # a modulo == 1 checks for odd numbers. If it was == 0, it would check for even numbers.
        print(i)

print()
print("We are going to use a `not` feature for this to see if it prints out the odd numbers.")

for i in range(1, 11):
    if not i % 2 == 0:      # using a `not` and `i % 2 == 0` does the same thing as just `i % 2 == 1`. Just do the latter.
        print(i)

# Step 2: Explore `while` loops.

print()
print("This is a countdown:")

countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")

print()
# Experiment with a condition where the user must enter a specific input to break the loop:

secret = "code"
user_input = ""
while user_input != secret:
    user_input = input("Guess the secret word: ")
print("You've guessed it!")

print()
# Step 3: Create a small project
# Guess the number game: 
# 1) The computer selects a random number between 1 and 20.
# 2) The user guesses, and the program provides feedback ("Too high!" or "Too low!") until the correct number is guessed.
# 3) Use a `while` loop to keep the game running.

import random       # the `random` library is imported into this script.

number_to_guess = random.randint(1, 20)     # The function calls (.) on `randint` to randomly choose a number `(1, 20)`, and it is pulled from the library `random`.
max_guesses = 3     # The user only has 3 guesses.
remaining_guesses = max_guesses

print("Guess the number between 1 and 20!")

user_guess = 0      # This variable has to equal a value that doesn't equal the variable `number_to_guess`.

while user_guess != number_to_guess and remaining_guesses > 0:
    if remaining_guesses == max_guesses:
        prompt_message = f"You have {remaining_guesses} guesses. Choose a number: "
    else:
        guess_word = "guess" if remaining_guesses == 1 else "guesses"       # Makes it singular/plural.
        prompt_message = f"You have {remaining_guesses} {guess_word} left. Choose another number: "
    
    user_input = input(prompt_message)

    if user_input.lower() == "stop":        # This is to let the user stop program immediately.
        print("Game stopped. Thank you for playing!")
        break       # This exits the loop immediately

    try:
        user_guess = int(user_input)
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 20, or type `stop` to quit.")
        continue    # This skips the rest of this iteration and re-prompts the user.

    remaining_guesses -= 1      # This subtracts 1 from the `remaining_guesses` variable.

    if user_guess < number_to_guess:
        print("Too low!")
    elif user_guess > number_to_guess:
        print("Too high!")
    else:
        print("Congratulations, you guessed it!")
        break       # This exits the loop if guessed correctly

if user_guess != number_to_guess and remaining_guesses == 0:
    print(f"Sorry, you're out of guesses! The correct number was {number_to_guess}.")









    #import random       # the `random` library is imported into this script.

#number_to_guess = random.randint(1, 20)     # The function calls (.) on `randint` to randomly choose a number `(1, 20)`, and it is pulled from the library `random`.
#max_guesses = 3     # The user only has 3 guesses.
#remaining_guesses = max_guesses

#print("Guess the number between 1 and 20!")
#print(f"You have {max_guesses} chances to guess right.")

#user_guess = 0      # This variable has to equal a value that doesn't equal the variable `number_to_guess`.

#while user_guess != number_to_guess and remaining_guesses > 0:
#    user_guess = int(input("Choose a number: "))
#    remaining_guesses -= 1      # This subtracts 1 from the `remaining_guesses` variable.

#    if user_guess < number_to_guess:
#        print("Too low!")
#        print(f"You have {remaining_guesses} guesses left!")
#    elif user_guess > number_to_guess:
#        print("Too high!")
#        print(f"You have {remaining_guesses} guess left!")
#    else:
#        print("Congratulations, you guessed it!")
#        break       # This exits the loop if guessed correctly

#if user_guess != number_to_guess:
#    print(f"Sorry, you're out of guesses! The correct number was {number_to_guess}.")