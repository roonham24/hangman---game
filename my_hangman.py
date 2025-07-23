import random
from words import words

def get_valid_word(words):
    word = random.choice(words)  # Randomly select a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words) 
    return word

def hangman():
    word = get_valid_word(words).upper()  # Get a valid word and convert it to uppercase
    word_letters = set(word)  # Create a set of letters in the word
    import string
    alphabet = set(string.ascii_uppercase)  # Set of uppercase letters
    used_letters = set()  # Set to keep track of used letters
    lives = 6  # Number of lives the player has

    # Getting User Input
    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))
        print("You have used these letters: ", ' '.join(used_letters))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # Remove the letter from the set if it's in the word
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()
