import random
def pick(word):
    """ Chooses a random word for the user to 
    guess based on their desired difficulty level 
    """
word_length = 0
difficulty = (input("Would you like to play the easy, normal or hard mode? ")).lower()
easy = [4, 5, 6]
normal = [6, 7, 8]
hard = [9, 10, 11]
if difficulty == "easy":
    word_length = random.choice(easy)
if difficulty == "normal":
    word_length = random.choice(normal)
if difficulty == "hard":
    word_length = random.choice(hard)
word = []
word_status = []
with open("words.txt") as words_file:
    for w in words_file.readlines():
        if len(w.strip()) == word_length: 
            word.append(w)
chosen_word = (random.choice(word)).lower()
for char in chosen_word.strip():
    word_status.append("_")
print(" ".join(word_status), "Your word contains", word_length, "letters")
print(chosen_word)


def new(round):
    print(mystery(word))

def mystery(word):
    """ Create a mystery word game 
    that allows users can select difficulty and guess a word 
    """
    guesses = [] 
    guesses_remaining = 8
    while guesses_remaining > 0 and word_status.count("_") != 0:
        letter_guess = (input("What letter would you like to guess? ").lower()) 
        while len(letter_guess) > 1:
            letter_guess = (input("Try again. Please only choose one letter: ").lower())
        if letter_guess in chosen_word:
            if letter_guess in guesses:
                print("Please guess again, you have already guessed that letter")
            else:
                for i in range(len(chosen_word)):
                    if letter_guess == chosen_word[i]:
                        word_status[i] = letter_guess
                        print(" ".join(word_status), "That letter is in the word!")
                        guesses.append(letter_guess)
            print("You have guessed the letters", guesses)
        if letter_guess not in chosen_word:
            if letter_guess in guesses:
                print("Please guess again, you have already guessed that letter")
            else:
                guesses.append(letter_guess)
                guesses_remaining = guesses_remaining - 1
                print(" ".join(word_status), "Chosen letter is not in the word, you have ", guesses_remaining, " guesses left")
                print("You have guessed the letters", guesses)
   
    if guesses_remaining == 0:
        print("No more guesses. Game Over. The correct word was", chosen_word)
        play_again = (input("Would you like to play again? ")).lower()
        if play_again == "yes":
            return new(round)
        else:
            print("Thank you for playing!")
    if word_status.count("_") == 0:
        print("Congrats, you have guessed the correct word!")
        play_again = (input("Would you like to play again? ").lower())
        if play_again == "yes":
            return new(round)
        else:
            print("Thank you for playing!")
print(mystery(difficulty))
