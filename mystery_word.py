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
with open("words.txt") as words_file:
   for w in words_file.readlines():
       if len(w.strip()) == word_length:
           word.append(w)
chosen_word = (random.choice(word))

print("Your word contains", word_length, "letters")
print(chosen_word)




# def display_letter(letter_guess, correct_guesses):
#     """
#     Show player how many spaces are remaining and where their correct letters appear
#     """
#     if letter_guess in correct_guesses: 
#         return letter_guess
#     else: 
#         return "_"
# return([display_letter(letter_guess,correct_guesses) for letter in chosen_word])
    
#return(correct_guesses, all_guesses)

def display_letter(letter_guess, correct_guesses):
    letter_guess = (input("What letter would you like to guess? ").lower())
    if letter_guess in correct_guesses: 
        return letter_guess
    else: 
        return "_"
print([display_letter(letter_guess,correct_guesses) for letter_guess in word])





def mystery(word):
    """ Create a mystery word game
    that allows users can select difficulty and guess a word """
    word_status = []
    guesses_remaining = 8
    all_guesses = []
    correct_guesses = []

    
    # if " ".join(word_status) == chosen_word:
    #    print("Congrats, you have guessed the correct word!")
    #    play_again = (input("Would you like to play again? ").lower())
    #    if play_again == "yes":
    #        return mystery(word)
    #    else:
    #        print("Thank you for playing!")

    if len(letter_guess) > 1:
       letter_guess = (input("Try again. Please only choose one letter: ").lower())
   #while guesses_remaining > 0:
    if letter_guess in all_guesses:
       print("Please guess again, you have already guessed that letter") 
    if letter_guess in chosen_word:
       #word_status = display_letter(letter_guess, correct_guesses)
       all_guesses.append(letter_guess)
       correct_guesses.append(letter_guess)
       game_status = display_letter(letter_guess, correct_guesses)
       print(game_status, "You have guessed", " ".join(all_guesses) )
    #    for char in chosen_word:
    #         if letter_guess in correct_guesses: 
    #             word_status.append(letter_guess)
    #         else: 
    #             word_status.append(" - ")
       print(word_status, "That letter is in the word!")
    if letter_guess not in chosen_word:
       all_guesses.append(letter_guess)
       guesses_remaining = guesses_remaining - 1
       print(word_status, "Chosen letter is not in the word, you have ", guesses_remaining, " guesses left")
 
    if guesses_remaining > 0:
       return mystery(word)
    else:
       print("No more guesses. Game Over. The correct word was", chosen_word)
       play_again = (input("Would you like to play again? ")).lower()
       if play_again == "yes":
           return mystery(word)
       else:
           print("Thank you for playing!")


print(mystery(difficulty))


