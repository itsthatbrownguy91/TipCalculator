#The Tip Calculator 

#Here, the initial price of the meal is asked from the user

price_meal = float(input("How much did your meal cost?: "))

#Next, the amount of people who will be splitting the bill is requested from the user

people = int(input("How many people will be splitting the bill?: "))

#Finally, The tip percentage is requested as a float from the use

tip = float(input("What percentage do you want to tip? Please include decimal point: "))

#First, the 10% tax is factored into the meal price, seperate from the tax.

tax_total = (price_meal * .10) + price_meal

#Next, The before-tax price of the meal is multiplied by the tip percentage float.

tip_total = (price_meal * tip)

#Then, The total from the meal price & the tax is added to the total from the meal price & the tip

meal_total = (tip_total + tax_total) 

#Finally, the meal total is divided by the amount of people inputted by the user

people_split = (meal_total / people)

#A statement is provide showing what the overall total is as well as the Per Person total in the currency format.

print(f'Your total cost is ${meal_total:,.2f} and each person will should pay ${people_split:,.2f}')

