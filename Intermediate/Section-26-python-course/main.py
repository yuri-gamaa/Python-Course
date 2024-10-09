import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

word = input("Insert a Word:\n\n: ").upper()

data_list = {row.letter: row.code for (index, row) in data.iterrows()
             if row.letter in word}

word_list = [data_list[w] for w in word]

print(word_list)
