from tkinter import *

# Set window
window = Tk()
window.title("Converter")
window.config(padx=40, pady=20)

# Text setup
text1 = Label(text="Miles")
text1.grid(column=2, row=0)
text2 = Label(text="is equal to ")
text2.grid(column=0, row=1)
text3 = Label(text="Km.")
text3.grid(row=1, column=2)
conversion = Label(text="0")
conversion.grid(column=1, row=1)

# Text entry
miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

# Button


def calculate():
    miles = miles_input.get()
    km = round(float(miles)*1.60934, 1)
    conversion["text"] = str(km)


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
