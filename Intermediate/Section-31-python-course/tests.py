import pandas
from random import randint, choice


# data = pandas.read_csv('en_words.csv')
# data['words'].to_clipboard()


data = pandas.read_csv("flashcard-app-db.csv")
print(data.columns[0])

row = randint(2, 494)
# word = [data.iloc[row, 0], data.iloc[randint(2, 494), 0]]
#
# run = True
# while run:
#     if word[1] == word[0]:
#         word[1] = data.iloc[randint(2, 494), 0]
#     else:
#         run = False

words = {
    "w": {
        "ptBR": data.iloc[row, 1],
        "en1": data.iloc[row, 0],
        "en2": data.iloc[randint(2, 494), 0]
    }
}

print(words["w"]["ptBR"])
print(words["w"]["en2"])
# del words["w"]["ptBR"]
#
# try:
#     print(words["w"]["ptBR"])
# except KeyError:
#     print(words)


# print(words["w"]["ptBR"] == words["w"]['ptBR'])

ptBR_id = data[data['Português'] == words['w']['ptBR']].index
en_id = data[data['Inglês'] == words['w']['en2']].index
# # print(value == other_value)
print(f"pt-BR: {ptBR_id}")
print(f"en: {en_id}")

if en_id[0] not in ptBR_id:
    print("hmmm")
else:
    print("Ok")
