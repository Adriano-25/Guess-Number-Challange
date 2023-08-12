import random

# Welcome message
print("Welcome to the Guess Number Challenge!")
print("Can you guess the secret number?")

# Ask for the player's name
player_name = input("What's your name? ")
print(f"Welcome, {player_name}!")

# Set the maximum number of attempts
max_attempts = 5

while True:  # Keep the game running until the player decides to stop
    # Generate a random secret number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    # Main game loop
    while attempts < max_attempts:
        try:
            # Ask the player for a guess
            guess = int(input("Take a guess: "))

            # Calculate the difference between the guess and the secret number
            difference = abs(guess - secret_number)

            if guess == secret_number:
                print(f"Congratulations, {player_name}! You guessed !{secret_number}!")
                break
            elif difference <= 10:
                print("Warm!")
            else:
                print("Cold!")
            
            # Increment the attempts counter
            attempts += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # If the player didn't guess the number
    if attempts == max_attempts:
        print(f"Sorry, {player_name}. You've reached the maximum number of attempts.")
        print(f"The secret number was {secret_number}. Better luck next time!")

    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()

    # Check if the player wants to play again
    if play_again != "yes":
        print("Thank you for playing Guess Number Challenge. Goodbye!")
        break
