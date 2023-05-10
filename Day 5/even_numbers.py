#Write your code below this row 👇
total = 0
counter = 0

for number in range(1, 101):
    if number % 2 == 0:
        total += number
        counter += 1

print(total)
