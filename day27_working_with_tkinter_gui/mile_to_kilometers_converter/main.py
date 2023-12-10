from tkinter import *


def convert():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_number.config(text=f"{float("{:.2f}".format(km))}")


window = Tk()
window.title("Miles to kilometer convert")
window.config(padx=20, pady=20)

is_equal_to_label = Label(text="is equal to:")
is_equal_to_label.grid(column=0, row=1)

miles_text_label = Label(text="Miles")
miles_text_label.grid(column=2, row=0)

km_text_label = Label(text="km")
km_text_label.grid(column=2, row=1)

miles_input = Entry(width=6)
miles_input.insert(END, string="0")
miles_number_int = miles_input.get()
miles_input.grid(column=1, row=0)

km_number = Label(text="0")
km_number.grid(column=1, row=1)

calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1, row=2)

window.mainloop()