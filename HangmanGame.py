# This program is a simple hangman game

from random import randint

words  = ['elephant', 'lion', 'tiger', 'fox', 'crocodile', 'monkey']
words += ['cow', 'sheep', 'horse','cat', 'dog', 'zibra', 'fish', 'wolf']
words += ['ant', 'donkey', 'chicken','hippopotamus', 'dog', 'giraffe']
words += ['bear', 'cheetah', 'whale','shark', 'rhino', 'gorilla']

hanged_man =      ['       O       ']
hanged_man.append ('+------|       ')
hanged_man.append ('|    -----     ')
hanged_man.append ('|   /  |  \    ')
hanged_man.append ('|      |       ')
hanged_man.append ('|    -----     ')
hanged_man.append ('===  |   |     ')

# A function to return a random word from a list of words
def get_word ():
    index = randint (0, len(words)-1)
    word = words[index].lower()
    return word

# This function takes a word and known_letters and written the word
# with known_letters exposed and the others covered with '*'
def expose_word (word, known_letters):
    for char in word:
        if char not in known_letters:
            word = word.replace(char, '*')
    return word

# Print the man hung up to a given level
def hang_man (level):
    if level > 7:
        level = 7
    for i in range (0, level):
        print (hanged_man [i])

# Return True if user wins, based on all letters in word are known
def is_winner (word, known_letters):
    word = expose_word (word, known_letters)
    if '*' not in word:
        return True
    else:
        return False
    
# Play the game
def main():
    word = get_word()       # Get random word from list
    trials = 7              # Set possible trials to 7
    given_letters = ''      # No letters are known yet

    while (trials > 0):     # While more trials
        char = ''
        while (len(char) != 1):     # Loop till user enters one letter only 
            char = input ("Please enter one letter guess: ")
        char = char.lower()

        given_letters = given_letters + char
        print (expose_word(word, given_letters))    # Print word with known
                                                    # letters uncovered 
        if char not in word:        # Reduce trials if letter not in word
            trials -= 1
            hang_man (7 - trials)

        if is_winner(word, given_letters):          # End if user wins
            print ("You Win")
            break

    if (trials == 0):               # If all trials finish, user loses
        print ("You lost - the secret word is ", word)
        
    
# Start the game 
main()
