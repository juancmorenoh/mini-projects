# Number of allowed attempts
attempts_allowed = 5

# Get the word to guess from the user and convert it to lowercase
chosen_word = input("Enter a word to guess: ").lower()

# Initialize a list to represent the word with underscores (for unguessed letters)
word = list()
guessed_letters = list()  # To track guessed letters

# Create the word with underscores (one for each letter in chosen_word)
for i in range(len(chosen_word)):
    word.append("_")

# Start the game loop
while attempts_allowed > 0 and "_" in word:
    
    # Display the current state of the word with blanks
    print(" ".join(word))
    
    # Ask the user to guess a letter
    guess = input("Enter a letter: ").lower()
    
    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue  # Skip the rest of the loop if the guess is repeated
    
    # Append the guess to the guessed_letters list
    guessed_letters.append(guess)

    # If the guessed letter is in the word, reveal its position(s)
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                word[i] = guess  # Update the word list with the correct guess

    else:
        # If the guessed letter is not in the word, reduce the number of attempts
        attempts_allowed -= 1
        print("You have ", attempts_allowed, " attempts left")

# Game over check: if attempts reach zero, the player loses
if attempts_allowed == 0:
    print("YOU LOSE")
else:
    # If all letters are guessed correctly, the player wins
    print("YOU WIN")
    print(" ".join(word))  # Display the final word with all correct guesses

