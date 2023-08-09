"""Little Codey is an interplanetary space boxer, who is trying to win championship belts for various weight categories on other planets within the solar system.

Write a space.py program that helps Codey keep track of their target weight by:
1. Checks which number planet is equal to.
2. It should then compute their weight on the destination planet.

Here is the table of conversions:
#	Planet	Relative Gravity
1	Venus	0.91
2	Mars	0.38
3	Jupiter	2.34
4	Saturn	1.06
5	Uranus	0.92
6	Neptune	1.19
"""
# Initialize variables
weight = 0
planet = 0 

# Start the program and display the planets for which we have gravity informationn available. 
print("Welcome to the space weight calculator!")
print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

# Ask for user inputs
input_weight = input("Enter your weight on Earth: ")
planet = input("Enter your destination planet number from the list above: ")

# Make user input weight into an integer
weight = int(input_weight)

# If statement loop that performs the calculation for each planet depending on user input for weight
# and planet number
if planet == "1":
    print(weight * 0.91)
elif planet == "2":
    print(weight * 0.38)
elif planet == "3":
    print(weight * 2.34)
elif planet == "4":
    print(weight * 1.06)
elif planet == "5":
    print(weight * 0.92)
elif planet == "6":
    print(weight * 1.19)
else:
    print("Invalid planet number entered, please try again")
    