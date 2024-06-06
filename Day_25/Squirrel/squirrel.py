import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# loop way (my method)

# gray_count = 0
# cinnamon_count = 0
# black_count = 0
#
# for index, row in data.iterrows():
#     if row["Primary Fur Color"] == "Gray":
#         gray_count += 1
#     elif row["Primary Fur Color"] == "Cinnamon":
#         cinnamon_count += 1
#     elif row["Primary Fur Color"] == "Black":
#         black_count += 1
#
# squirrel_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_count, cinnamon_count, black_count]
# }

# I guess it has lesser complexity

grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])

squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, cinnamon_squirrels, black_squirrels]
}

squirrel_data = pd.DataFrame(squirrel_dict)

squirrel_data.to_csv("color_count.csv", index=False)
