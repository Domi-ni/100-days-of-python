from tkinter import *

window = Tk()
window.title("My first Tkinter GUI program")
window.minsize(width=500, height=300)

new_label = Label(text="I am a label", font=("Arial", 15, "bold"))
new_label.grid(column=0, row=0)

button = Button(text="I am a button")
button.grid(column=1, row=1)

new_button = Button(text="I am a new button")
new_button.grid(column=2, row=0)

input = Entry()
print(input.get())
input.grid(column=3, row=3)

window.mainloop()
