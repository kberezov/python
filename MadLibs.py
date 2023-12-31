"""
Description: This is a Python Mad Libs game
Author: Kate
"""

# The template for the story
STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

# The inputs for the story
print("The Mad Libs game has started")
name = input("Enter a name: ")
adj1 = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
adj3 = input("Enter one more adjective: ")
verb = input("Enter a verb: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
animal = input("Enter any animal: ")
food = input("Enter any food: ")
fruit = input("Enter any fruit: ")
superhero = input("Enter any superhero: ")
country = input("Enter any country: ")
dessert = input("Enter any dessert: ")
year = input("Enter any year: ")

# Printing the story
print(STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2))