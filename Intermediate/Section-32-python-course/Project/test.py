# with open('letter_templates/letter_1.txt', 'r') as file:
    # data = file.read()
# print(data)

# with open('letter_1.txt', 'a') as file:

import json

# with open('check_letters.json', 'w') as file:
#
#     dict_ = {
#         "person1": [],
#         "person2": []
#     }
#
#     json.dump(dict_, file, indent=4)

with open('check_letters.json', 'r') as file:
    data = json.load(file)


def key(dict_, position):
    i = 0
    try:
        for (k, v) in dict_.items():
            if i == position:
                return k
            i += 1
    except KeyError:
        return None
#
#
# print(key(data, 3))

for _ in data:
    print(_)
