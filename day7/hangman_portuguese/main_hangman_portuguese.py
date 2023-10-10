import random
from hangman_images import stages, logo
from hangman_words import word_list

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(f"{logo}\n")

display = []
for space in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("Chute uma letra: ").lower()
    if guess in display:
        print(f'\nVocê ja tentou essa letra "{guess}"')

    for position in range(word_length):
        letter = chosen_word[position]

        if guess == letter:
            display[position] = guess

    print(f"\n{' '.join(display)}\n")

    if guess not in chosen_word:
        lives -= 1
        print(
            f"Você chutou {guess}, essa letra nao esta na palavra. Você perde uma vida."
        )
        print(stages[lives])

    if lives == 0:
        end_of_game = True
        print(f"Você perdeu, a palavra era {chosen_word}")

    if not "_" in display:
        end_of_game = True
        print("Você ganhou!")
