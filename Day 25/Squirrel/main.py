import pandas as pd

squirrel_data = pd.read_csv("./day 25/squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = squirrel_data["Primary Fur Color"]
gray_fur = len(squirrel_data[fur_color == "Gray"])
red_fur = len(squirrel_data[fur_color == "Cinnamon"])
black_fur = len(squirrel_data[fur_color == "Black"])

# print(fur_color)
print(gray_fur)
print(red_fur)
print(black_fur)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_fur, red_fur, black_fur]
}

df = pd.DataFrame.from_dict(data_dict)

df.to_csv("./day 25/squirrel/squirrel_fur_color_count.csv")