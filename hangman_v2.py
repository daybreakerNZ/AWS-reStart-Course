# Hangman
# AWS re/Start course
# learning python progamming

import time
import string
import random
import json

# Step 1 - find a random word to use

dictionary_data = json.load(open("dictionary.json"))
number_of_words = len(dictionary_data)
random_number = random.randint (1,number_of_words)
word_count = 0
for item in dictionary_data:
	word_count = word_count + 1
	if word_count == random_number:
		hangman_word = item
		break

# Set up variables

total_tries = [
	"hangmans platform",
	"the posts",
	"the crossbeam",
	"the rope",
	"body",
	"legs",
	"arms",
	"neck",
	"head",
	"trapdoor"
]

unsuccessful_tries = []

number_of_characters = len(hangman_word)
hangman_string = ""
guessed_it = False

while len(hangman_string) < len(hangman_word):
	hangman_string = hangman_string + "_"

# You can uncomment if debugging
#print (hangman_word)
#print (hangman_string)


#Step 2 - set up a while loop until either player has run out of tries or guessed the word

while (hangman_string.find('_' ) != -1):

	print(unsuccessful_tries)

	print(hangman_string)

	letter_guess = input("Choose a character from a-z : ")

	# when guessing the whole word
	if hangman_word == letter_guess:
		guessed_it = True
		break
	elif len(letter_guess) == 1:
		letter_exists = False
		counter = 0
		for a_letter in hangman_word:
			if letter_guess == a_letter:
				s= list(hangman_string)
				s[counter] = letter_guess
				hangman_string = "".join(s)
				letter_exists = True
			counter = counter + 1
		if letter_exists == False:
			if len(total_tries) > 0:
				unsuccessful_tries.append(total_tries[0])
				del total_tries[0]
			else:
				guessed_it = False
				break
	elif letter_guess == "":
		time.sleep(1)
		#otherwise do nothing


print(unsuccessful_tries)
print (hangman_string)
		
if guessed_it == True or hangman_string == hangman_word:
	print("Yes " + hangman_word + " is correct. Congratulations. You saved yourself from the noose just in time")

else:
	print("Hangman! You have run out of chances - the word is " + hangman_word);

exit(1)