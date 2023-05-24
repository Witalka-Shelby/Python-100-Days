file_1_list = []
file_2_list = []

with open("./day 26/file1.txt") as file1:
    for num1 in file1:
        file_1_list.append(int(num1.replace('\n', "")))

with open("./day 26/file2.txt") as file2:
    for num2 in file2:
        file_2_list.append(int(num2.replace('\n', "")))

# print(file_1_list)
# print(file_2_list)

result = [x for x in file_1_list if x in file_2_list]
# Write your code above 👆

print(result)


