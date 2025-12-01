import random
# Import the random module to generate a random number

# Generate a random number between 1 and 9
number_to_guess = random.randint(1, 9)

# Start a loop that ends when the user guesses correctly
while True:
    # Ask the user to enter a guess
    guess = input("Guess a number between 1 and 9 --->")

    # Check if the input is actually a number (not letters or symbols)
    if not guess.isdigit():
        print("Please enter a valid number --->")
        continue
        # Skip the rest of the loop and prompt again

    # Convert the valid input to an integer
    guess = int(guess)

    # Check if the user's guess matches with the random number
    if guess == number_to_guess:
        print("Correct!!!")
        break
        # Exit the loop (end program)
    else:
        # The guess was wrong, so prompt the user again
        print("Incorrect, try again.")
