alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

from art import logo

restart = True
print(logo)


def caesar(chosen_direction, user_text, shift_amount):
    """
    Encode or decode a piece of text, basead in the direction that was given
    """
    final_text = ""

    for char in user_text:
        if char in alphabet:
            if char == alphabet[alphabet.index(char)]:
                if chosen_direction == "encode":
                    final_text += alphabet[alphabet.index(char) + shift_amount]
                if chosen_direction == "decode":
                    final_text += alphabet[alphabet.index(char) - shift_amount]
        else:
            final_text += char

    print(f"The {chosen_direction}d text is {final_text}")


while restart == True:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % 26

    caesar(chosen_direction=direction, user_text=text, shift_amount=shift)
    go_again = input(
        "\nType 'yes' if you want to go again. Otherwise type 'no':\n"
    ).lower()

    if go_again == "no":
        restart = False
