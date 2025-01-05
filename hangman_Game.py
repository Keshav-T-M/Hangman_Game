import random

#this function return random word
def choose_word():
    words = ["python", "java", "javascript", "kotlin", "swift", "ruby", "csharp", "go", "typescript", "php","keshav","hangman"]
    return random.choice(words).upper()
