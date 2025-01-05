import random

#this function return random word
def choose_word():
    words = ["python", "java", "javascript", "kotlin", "swift", "ruby", "csharp", "go", "typescript", "php","keshav","hangman"]
    return random.choice(words).upper()



def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_guesses = 6  

    print("Welcome to Hangman!")