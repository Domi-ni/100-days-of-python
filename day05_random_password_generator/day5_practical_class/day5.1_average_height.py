# not using any method, it's to pratice for loops

number_of_students = 0
heights_sum = 0

student_heights = input().split()
for height in range(0, len(student_heights)):
    student_heights[height] = int(student_heights[height])

for height in student_heights:
    number_of_students += 1
    heights_sum += height
averege_height = round(heights_sum / number_of_students)
print(f"total height = {heights_sum}")
print(f"number of students = {number_of_students}")
print(f"average height = {averege_height}")
