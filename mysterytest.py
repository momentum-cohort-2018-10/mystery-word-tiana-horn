# import random

# word_length = 0
# difficulty = (input("Would you like to play the easy, normal or hard mode? ")).lower()
# easy = [4, 5, 6]
# normal = [6, 7, 8]
# hard = [9, 10, 11]
# if difficulty == "easy":
#    word_length = random.choice(easy)
# if difficulty == "normal":
#    word_length = random.choice(normal)
# if difficulty == "hard":
#    word_length = random.choice(hard)

# word = []
# word_status = []
# with open("words.txt") as words_file:
#    for w in words_file.readlines():
#        if len(w.strip()) == word_length:
#            word.append(w)
# chosen_word = (random.choice(word))

# guesses = []
# print(chosen_word)
# letter_guess = (input("What letter would you like to guess? ").lower())

# def display_word(chosen_word, guesses):

#     if letter_guess in chosen_word.strip():
#       return letter_guess
#     else:
#       return "_ "
      
# print([display_word(chosen_word,guesses) for letter in chosen_word])







letter = (input("What letter would you like to guess? ").lower())
word = "happy"
correct_guesses = ["a", "p", ]
all_guesses = ["a", "p", "z"]

def display_letter(letter, guesses):
    if letter in correct_guesses: 
        return letter
    else: 
        return "_"
print([display_letter(letter,correct_guesses) for letter in word])


# for char in chosen_word:
#     if letter_guess in correct_guesses: 
#         return letter_guess
#     else: 
#         return "-"
# print(word_status)



# import random
# def play_game():
#     print_instructions()
#     number_to_guess = random.randint(1,1000)
#     number_guessed = False
#     guesses = 0
#     while not number_guessed and guesses < 10:
#         guess = input_integer("What’s your guess? ", min=1, max=100)
#         guess = int(guess)
#         if guess == number_to_guess:
#             print("You got it right!")
#             number_guessed = True
#         elif guess < number_to_guess:
#             print("Too low!")
#         else:
#             print("Too high!")
			



# def print_instructions():
# 	print("I am going to choose a number between 1 and 10000. You have 10 guesses to get it right.")

# def input_integer(prompt, min=None, max=None):

# 	guess = input(prompt)
# 	while not is_integer(guess) and within_range(int(guess, 1, 1000)):
# 		print("Invalid input")
# 		guess = input(prompt)
# 	return guess

# def is_integer(string):
# 	return string.isdigit()

# def within_range(number, min=None, max=None):
# 	if min is not None and number < min:
# 		return False
# 	if max is not None and number > max:
# 		return False
# 	return True

# print(play_game())
