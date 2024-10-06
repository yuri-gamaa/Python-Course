import pandas

data = pandas.read_csv('../weather_data.csv')
temperatures = data["temp"]
# print(temperatures)
# print(f'\nAverage: {temperatures.mean()}')
# print(f'Maximum value: {temperatures.max()}')

value = data[data.day == "Friday"]["day"]
# print(type(value))

convert_it = data[data.day == "Monday"]['temp'] * 9/5 + 32

# print(convert_it)

# 29-30/09/24 (Máxima e Mínima)
weather_cuiaba = {
    "domingo": {
        "max": 40,
        "min": 27
    },
    "segunda-feira": {
        "max": 39,
        "min": 27
    }
}

data = pandas.DataFrame(weather_cuiaba)
print(data)
data.to_csv('clima_cuiabá.csv', encoding="utf-8")
