# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

#Write your code below this line 👇
bmi = weight / height ** 2
if bmi < 18.5:
    print(f"Your BMI is {round(bmi)}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {round(bmi)}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {round(bmi)}, you are obese.")
else:
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")