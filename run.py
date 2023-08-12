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
