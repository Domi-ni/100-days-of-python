row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print("     1     2     3")
print(f"1 {row1}\n2 {row2}\n3 {row3}")
position = input(
    "Where do you want to put the treasure? (Column as first number, row second as number) "
)

column_number = int(position[0]) - 1
row_number = int(position[1]) - 1
map[row_number][column_number] = " X"

print(f"{row1}\n{row2}\n{row3}")
