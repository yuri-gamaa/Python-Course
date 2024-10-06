with open('../weather_data.csv', 'r') as file:
    content = file.readlines()

import csv

with open('../weather_data.csv') as file:
    data = csv.reader(file)
    data_list = [temp for temp in data]
    temperatures = [data_list[temp][1] for temp in range(1, len(data_list))]
    # print(temperatures)
    # for line in data:
    #     pass
    #     print(type(data))

import pandas

data = pandas.read_csv('../weather_data.csv')
print(data["temp"])
