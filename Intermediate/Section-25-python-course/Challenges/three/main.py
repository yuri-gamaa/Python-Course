import pandas

# My way:
# data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240930.csv')
#
# dict_csv = {}
# pfc = "Primary Fur Color"
# selected_colors = data[pfc].unique().tolist()
# amount = data[pfc].value_counts().tolist()
#
# for item in range(1, len(selected_colors)):
#     dict_csv[selected_colors[item]] = amount[item-1]
#
# print(dict_csv)
#
# content = pandas.DataFrame([dict_csv])
# content.to_csv("cores_esquilos.csv")
#
# with open('cores_esquilos.csv') as file:
#     test = file.read()
#     print(test)

# Teacher way:
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240930.csv')
grey = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

# Then she created a dictionary
# After use DataFrames()
# And convert to a cvs file
