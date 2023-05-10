print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
price_per_person = bill / people
calc = (price_per_person + ((price_per_person) / 100 * percent))
calc = "{:.2f}".format(calc)
print(f"Each person should pay: ${calc}")