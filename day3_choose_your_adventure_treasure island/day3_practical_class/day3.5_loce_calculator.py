print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_name = name1 + name2
combine_name = combine_name.lower()
number_of_t = combine_name.count("t")
number_of_r = combine_name.count("r")
number_of_u = combine_name.count("u")
number_of_e = combine_name.count("e")
total_true = number_of_t + number_of_r + number_of_u + number_of_e
number_of_l = combine_name.count("l")
number_of_o = combine_name.count("o")
number_of_v = combine_name.count("v")
number_of_e = combine_name.count("e")
total_love = number_of_l + number_of_o + number_of_v + number_of_e
total = int(str(total_true) + str(total_love))
if total <= 10 or total >= 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
