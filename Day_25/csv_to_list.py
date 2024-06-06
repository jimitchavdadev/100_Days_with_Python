# csv to list

# weather_list=[]
# with open("weather_data.csv") as data:
#     weather = data.readlines()
#     weather_list.append(weather)
#
# print(weather_list)

# extracting a column

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temparature=[]
#     for row in data:
#         temp = row[1]
#         temparature.append(temp)

import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()


# some statistical operations
# avg = data["temp"].mean()
# print(avg)
# median = data["temp"].median()
# print(median)
# mode = data["temp"].mode()
# print(mode)
# max = data["temp"].max()
# print(max)

def c_to_f(value):
    value = 1.8 * value + 32
    return value


# getting a single row for some condition
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# celcius to fahrenheit
# data["temp"] = c_to_f(data["temp"])
# print(data["temp"])

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
