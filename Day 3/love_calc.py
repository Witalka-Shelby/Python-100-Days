# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
counter1 = 0
counter2 = 0
name1 = name1.lower()
name2 = name2.lower()

if "t" in name1 or "t" in name2:
    counter1 += name1.count("t")
    counter1 += name2.count("t")
if "r" in name1 or "r" in name2:
    counter1 += name1.count("r")
    counter1 += name2.count("r")
if "u" in name1 or "u" in name2:
    counter1 += name1.count("u")
    counter1 += name2.count("u")
if "e" in name1 or "e" in name2:
    counter1 += name1.count("e")
    counter1 += name2.count("e")

if "l" in name1 or "l" in name2:
    counter2 += name1.count("l")
    counter2 += name2.count("l")
if "o" in name1 or "o" in name2:
    counter2 += name1.count("o")
    counter2 += name2.count("o")
if "v" in name1 or "v" in name2:
    counter2 += name1.count("v")
    counter2 += name2.count("v")
if "e" in name1 or "e" in name2:
    counter2 += name1.count("e")
    counter2 += name2.count("e")

love_count = int(str(counter1) + str(counter2))

if love_count < 10 or love_count > 90:
    print(f"Your score is {love_count}, you go together like coke and mentos.")
elif love_count > 40 and love_count < 50:
    print(f"Your score is {love_count}, you are alright together.")
else:
    print(f"Your score is {love_count}.")

