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
