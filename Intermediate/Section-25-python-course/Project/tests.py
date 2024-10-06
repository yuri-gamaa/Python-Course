from datetime import timedelta
from turtle import Screen
# for i in range(1, 10):
#     rs = timedelta(minutes=i, seconds=0, milliseconds=0) % timedelta(minutes=1)

micro = timedelta(minutes=1, seconds=0)
micro -= timedelta(seconds=1)

# print(micro)

# s = Screen()
# value = s.textinput("State", "Insert a State from USA")
# print(value.lower())
# s.exitonclick()

import pandas
data = pandas.read_csv('50_states.csv')
list_test = data['state'].tolist()
# random_x = data[data['x'] == -297].to_list()
# print(len(list_test))
# list_test = [print(rs.upper()) for rs in list_test]
# string = data[data['state'] == Texas]


number = 1233
s_number = str(number)[1:2]
# print(s_number)

ten_states = [
    "California",
    "Texas",
    "Florida",
    "New York",
    "Pennsylvania",
    "Illinois",
    "Ohio",
    "Georgia",
    "North Carolina",
    "Michigan"
]

five = ten_states[:5]

if five[0:] in ten_states:
    pass
    # print('ok')           ESSE NÃO ROLOU!


