# import csv

# data = []

# with open("weather_data.csv") as weather_data:
#         data = csv.reader(weather_data)
#         temps = []
#         for temp in data:
#             # print(temp[1])
#             if "temp" in temp:
#                 continue

#             temps.append(int(temp[1]))


import pandas as pd

panda_data = pd.read_csv("weather_data.csv")
temps = panda_data["temp"]

# print(panda_data.temp)

# print(temps.max())

print(panda_data["temp"] == panda_data["temp"].max())