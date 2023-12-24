import pandas


def convert_word():
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    # print(nato_phonetic_df_dict)

    word = input("Insert the word: ").upper()

    try:
        list_of_words = [data_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter in the alphabet please \n")
        convert_word()
    else:
        print(list_of_words)


convert_word()
