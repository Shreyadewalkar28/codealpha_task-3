import random

# List of predefined words
words = ["cloud", "space", "magic", "apple", "river"]

def play_game():
    word = random.choice(words)
    guessed = []
    tries = 6
    
    display = ['_'] * len(word)

    print("\n🎮 Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print(f"You have {tries} incorrect guesses.\n")

    while tries > 0 and '_' in display:
        print("Word:", " ".join(display))
        print("Guessed letters:", guessed)
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❗ Please enter a single letter.\n")
            continue

        if guess in guessed:
            print("⚠ You already guessed that!\n")
            continue

        guessed.append(guess)

        if guess in word:
            print("✅ Correct!\n")
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
        else:
            tries -= 1
            print(f"❌ Incorrect! {tries} tries left.\n")

    if "_" not in display:
        print("🎉 You WON! The word was:", word)
    else:
        print("💀 You lost! The word was:", word)

# Replay loop
while True:
    play_game()
    replay = input("\n🔁 Do you want to play again? (yes/no): ").lower()
    if replay != 'yes':
        print("👋 Thanks for playing! See you next time.")
        break