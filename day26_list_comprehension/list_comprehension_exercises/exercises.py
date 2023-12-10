# squared numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [number * number for number in numbers]
print("squared numbers:")
print(squared_numbers)

# filtering even numbers
list_of_strings = input("\n put a list of numbers split by a coma (,): ").split(',')

even_numbers = [int(number) for number in list_of_strings if int(number) % 2 == 0]
print("filtering even numbers:")
print(even_numbers)

# dictionary comprehension
# split the sentence and count how many letters each word has

sentence = input("\n write a sentence: ")

new_list = sentence.split(" ")
result = {word: len(word) for word in new_list}
print(result)

# convert Celsius weather in to Fahrenheit
weather_c = {"Monday": 4, "Tuesday": 5, "Wednesday": 10, "Thursday": 11, "Friday": 12, "Saturday": 14, "Sunday": 16}

weather_f = {week_day:(temp_c * 9/5) + 32 for (week_day, temp_c) in weather_c.items()}
print("\n converting to Fahrenheit: ")
print(weather_f)
