# Define variables
pyg = 'ay'
vowels = 'aeiou'

# Define functions
def ask():
    original = raw_input('Enter a word: ')
    translate(original)


def again():
    answer = raw_input('Would you like to give it another go? ')
    answer = answer.lower() # Formats the answer
    answer = answer[0]      # into a simple 'y'
    if answer == 'y':
        return True
    else:
        return False


def translate(word):
    if len(word) > 0 and word.isalpha():
        word = word.lower() # Set all the letters in the word to lowercase
        first = word[0] # Add a variable with the value of the first letter of word

        # Checking if the word starts with a vowel or consonant
        if first in vowels:
            word += pyg # Add 'ay' to the end of the word
        else:
            word = word[1:] + first + pyg # Put the first letter of the word on the end and add 'ay'

        print 'Your word in Pig Latin is ' + word
        if again():
            ask()
        else:
            print 'Thank you for using PYG LATIN TRANSLATOR'
    else:
        print 'You need to enter an English word.'
        print 'If you do not understand why you got this message, try typing it without numbers and make sure it is only ONE word'
        ask()


print 'Welcome to PYG LATIN TRANSLATOR. Type in any word and it automatically translates it into Pig Latin. Revolutionary!'
ask()
