import os

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Set current work path to where this py file is
os.chdir(os.path.dirname(os.path.abspath(__file__)))

letter_txt = "./Input/Letters/starting_letter.txt"
names_txt = "./Input/Names/invited_names.txt"

output_path = "./Output/ReadyToSend/"

names_list = []
letter = ""

with open(names_txt) as names:
    for name in names:
        names_list.append(name.replace("\n", ""))

with open(letter_txt) as text:
    letter = text.read()

for name in names_list:
    with open(f"{output_path}{name}.txt", "w") as output:
        output.write(letter.replace("[name]", name))