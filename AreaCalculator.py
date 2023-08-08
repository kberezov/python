"""This program is a calculator that can compute the are of a circle and a triangle"""

print("The calculator is starting up")

option = input("Enter C for Circle or T for triangle: ")

if option.lower() == "c":
  radius = float(input("Enter the radius: "))
  area = (radius ** 2) * 3.14159
  print("The area is %f" % area)
elif option.lower() == "t":
  base = float(input("Enter the base of the triangle: "))
  height = float(input("Enter the height of the triangle: "))
  area = base * height * 0.5
  print("The area is %f" % area)
else:
  print("Invalid input, try again")

print("See you later, alligator")