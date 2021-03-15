# weather_cond =[]
# with open("weather_data.csv") as data:
#     weather = data.readlines()
#     for row in weather:
#         weather_cond.append(row.strip())

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] == "temp":
#             pass
#         else:
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# Use column name to call data
# print(data["temp"])
# Type dataframe = table
# print(type(data))
# Type dataseries = column
# print(type(data["temp"]))

# # Convert to dictionary
# data_dict = data.to_dict()
# print(data_dict)
# # Convert series to list
# temp_list = data["temp"].to_list()
# print(temp_list)

# # Manual average calculation
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
# # Pandas method
# print(data["temp"].mean())
# print(data["temp"].max())

# # Getting a series, Pandas turns the headings into attributes:
# print(data["condition"])
# print(data.condition)

# # Getting data by rows, pandas looks for the filter in the column
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# temp_f = (int(monday.temp) * 9 / 5) + 32
# print(temp_f)

# How to create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# new_data = pandas.DataFrame(data_dict)
# print(new_data)
# new_data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_dict = {
    "Gray": 0,
    "Cinnamon": 0,
    "Black": 0
}

for color in data["Primary Fur Color"]:
    if color in squirrel_dict:
        squirrel_dict[color] += 1

new_dict = {
    "Fur Color": [],
    "Count": []
}

for color in squirrel_dict:
    new_dict["Fur Color"].append(color)
    new_dict["Count"].append(squirrel_dict[color])

new_data = pandas.DataFrame(new_dict)
new_data.to_csv("squirrel_count.csv")



