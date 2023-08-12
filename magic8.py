#Background
"""A magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.

Magic 8-Ball, should I do this project?

We’ll be using the following 9 possible answers for our Magic 8-Ball:

Yes - definitely
It is decidedly so
Without a doubt
Reply hazy, try again
Ask again later
Better not tell you now
My sources say no
Outlook not so good
Very doubtful
The output of the program will have the following format:

[Name] asks: [Question]
Magic 8-Ball’s answer: [Answer]"""

#Import modules
import random

#Intialize variables
name = ""
question = ""
answer = ""
random_number = random.randint(1,11)

#If block for the numbers and answers
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Go back to bed instead"
elif random_number == 11:
  answer = "Its 50/50"
else:
  answer = "Error"

#Ask for name and question user input
name = input("Enter your name: ")
question = input("Enter your question for the magic 8-Ball: ")

#If block for when the name is not provided
if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)

#If block for when the question is not provided
if question == "":
  print("You need to enter a question!")
else:
  print("\nMasic 8-Ball's answer: " + answer)

print("\nGoodbye\n")

