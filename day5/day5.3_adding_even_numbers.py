target = int(input())
even_numbers_sum = 0
for number in range(2, target + 1, 2):
    even_numbers_sum += number
print(even_numbers_sum)
