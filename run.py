import random


# Welcome message
print("Welcome to the Guess Number Challange!")
print("Can you guess the secret number?")

# Ask for the player's name
player_name = input("What is your name? ")

# Generate a random secret number beetween 0 and 100
secret_number = random.randint(1, 100)

# Desplay a secret number for testing purpose
print(f"DEBUG: Secret number is {secret_number}")

# Set the maximum number of attempts
max_attempts = 5
attempts = 0

# Set the maximum number of attempts
max_attempts = 5
attempts = 0

# Main game loop
while attempts < max_attempts:
    # Ask the player for a guess
    guess = int(input("Take a guess: "))
# Set the maximum number of attempts
max_attempts = 5
attempts = 0

# Main game loop
while attempts < max_attempts:
    # Ask the player for a guess
    guess = int(input("Take a guess: "))

    if guess == secret_number:
        print(f"Congratulations, {player_name}! You guessed{secret_number}!")
        break
    elif guess < secret_number:
        print("To low! Try a higher number.")
    else:
        print("To high! Try a lower number.")

        attempts += 1

if attempts == max_attempts:
    print(f"Sorry, {player_name}. You reach the maximum number of attempts.")
    print(f"The secret number was {secret_number}. Better luck next time!")
