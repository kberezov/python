# What is Pig Latin
'''Pig Latin is a language game, where you move the first letter of the word to the end and add “ay.” So “Python” becomes “ythonpay.” To write a Pig Latin translator in Python, here are the steps we’ll need to take:
1. Ask the user to input a word in English.
2. Make sure the user entered a valid word.
3. Convert the word from English to Pig Latin.
4. Display the translation result.'''

# initializes important variables
pyg = 'ay'
original = input('Enter a word:')

# the if statemnt checks that user input is not blank and only contains letters, if not, returns 'empty'
if len(original) > 0 and original.isalpha():
  word = original.lower()
  print(original)
else:
  print('empty')

# takes the first letter of user input in lower case
first = word[0]

# takes the user input word in lower case without the first letter, adds the first letter to the end of the word, and adds 'ay' to the end of the new word
new_word = word[1:] + first + pyg
print(new_word)