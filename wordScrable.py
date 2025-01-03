import random

print("Welcome to the Word Scramble Game!")
print("Unscramble the letters to guess the word.\n")

# List of words
words = ["python", "guitar", "elephant", "rainbow", "computer", "pizza", "airplane", "chocolate", "unicorn"]

# Pick a random word
word = random.choice(words)
scrambled = ''.join(random.sample(word, len(word)))

print(f"Scrambled word: {scrambled}")

# Let the user guess
attempts = 3
while attempts > 0:
    guess = input("Your guess: ").lower()
    if guess == word:
        print("🎉 Correct! You guessed it!")
        break
    else:
        attempts -= 1
        print(f"❌ Wrong! You have {attempts} attempt(s) left.")

if attempts == 0:
    print(f"Game Over! The correct word was '{word}'. Better luck next time!")
