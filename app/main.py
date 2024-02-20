#Today's lessons will cover For & While Loops, IF/ELSE, Lists, Strings, Range, and Modules

#Build Hangman game
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
Sorry, GAME OVER...
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
Uh oh, there the right leg, you're down to one more try!
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
Here comes the left arm!
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
I see a right arm!
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
Here comes the Mid-Section!
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
Oh man! There goes the Head!
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
Uh Oh, there goes the platform!
''']

#Declaration of variabale and File opener
word_list   = []

#Open file from a text document of names
#Open the text file
with open('names.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Strip whitespace/newline and add to the list
        word_list.append(line.strip())

chosen_word = ""
rand_index  = random.randint(0, len(word_list)-1)
save_letter = []
check_list  = []
game_over   = False
lives       = 7
letter_check = False

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

#Random generated word from list
chosen_word = word_list[rand_index]

#Add that word to a check from list
for index in range(len(chosen_word)):
    check_list += chosen_word[index]

#Welcome Banner
print(logo)

#Prompt for Word
print("\nThe selected word has " + str(len(chosen_word)) + " characters in it. See below.")

#So the blanks for the chosen word
for index in range(len(chosen_word)):
    save_letter += "_"
    if(index == len(chosen_word) - 1):
        print(save_letter)

#Hangman Game
#While loop to loop through until End of Game is True
while(game_over == False):
    #Guess input prompt
    guess  = input("\nGuess a letter in the word: ").lower()

    #For loop to iterate the gues character through the chosen word
    for index in range(0, len(chosen_word)):
        letter = chosen_word[index]
        if(letter == guess):
            save_letter[index] = letter
            letter_check = True

    #Boolen Check for letter_check
    if(letter_check == True):
        result_sl   = ' '.join(save_letter)
        print(result_sl)
        letter_check = False
    else:
        result_sl   = ' '.join(save_letter)
        lives = lives - 1
        print(stages[lives])
        print("Ouch! You have " + str(lives) + " lives left!")
        print(result_sl)

    #Game Over Condition
    if(save_letter == check_list):
        game_over = True
        print("You've Won!!!")
    elif(lives == 0):
        game_over = True
        print("The name you were trying to guess was :" + str(chosen_word))