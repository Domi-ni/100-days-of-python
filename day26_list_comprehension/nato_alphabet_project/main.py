import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_phonetic_df_dict)

word = input("Insert the word: ").upper()
list_of_words = [data_dict[letter] for letter in word]
print(list_of_words)
