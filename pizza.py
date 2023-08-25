"""Len's Slice
You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data."""

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

#find the number of $2 slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#find the number of toppings
num_pizzas = len(toppings)

#pring a message
print("We sell %d different kinds of pizza!" % num_pizzas)

#create a two dimensional list, each sublist should have one pizza topping and an associate price
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
#print(pizza_and_prices)

#sort pizza_and_prices so that pizzas are in order of increasing price
pizza_and_prices.sort()
print(pizza_and_prices)

#Store the first element of pizza_and_prices in a variable called cheapest_pizza
cheapest_pizza = pizza_and_prices[0]

#Find the priciest pizza
priciest_pizza = pizza_and_prices[-1]

#It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice
pizza_and_prices.pop()

#add a new pizza [2.5, "peppers"] to the list. Make sure to put it at the right index to keep the sorted order
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

#Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)













