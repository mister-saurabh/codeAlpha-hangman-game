import random

# List of possible words for the game
word_list = ['python', 'developer', 'hangman', 'challenge', 'programming', 'keyboard']

# Choose a random word from the list
chosen_word = random.choice(word_list)

# Create a list of underscores the same length as the chosen word
display = ['_' for x in chosen_word]

# Number of lives the player has
lives = 6

# List to keep track of guessed letters
guessed_letters = []

# Display game instructions
print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have", lives, "lives.")
print(" ".join(display))  # Show initial display (all underscores)

# Game loop
while lives > 0 and '_' in display:
    guess = input("Guess a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)

    # If the guess is in the chosen word
    if guess in chosen_word:
        # Reveal the correct letters in the display
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print("Correct guess!")
    else:
        # Deduct a life for a wrong guess
        lives -= 1
        print(f"Wrong guess! You have {lives} {'life' if lives == 1 else 'lives'} left.")

    # Show the current state of the word
    print(" ".join(display))
    print()

# Game over messages
if '_' not in display:
    print("Congratulations! You guessed the word:", chosen_word)
else:
    print("Game Over! The word was:", chosen_word)
