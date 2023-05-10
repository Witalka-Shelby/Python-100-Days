def format_name(name, surname):
    f_name = name.capitalize()
    l_name = surname.capitalize()
    print(f"{f_name} {l_name}")

name1, name2 = input("Enter full name").split()
format_name(name=name1, surname=name2)