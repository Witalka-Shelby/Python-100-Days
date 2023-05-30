import pandas

nato_list = pandas.read_csv("./day 26/nato_phonetic_alphabet.csv")

phone_dict = {row.letter: row.code for (index, row) in nato_list.iterrows()}

def gen_phonetic():
    name_input = input("Enter Name: ").upper()
    try:
        nato_name_list = [phone_dict[letter] for letter in name_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        gen_phonetic()
    else:
        print(nato_name_list)

gen_phonetic()