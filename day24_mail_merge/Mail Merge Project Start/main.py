with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as initial_letter:
    letter = initial_letter.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)
