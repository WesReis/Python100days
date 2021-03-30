from tkinter import *

# Variables
window = Tk()
# Custom title
window.title("My first GUI program.")
# size in pixels
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label.", font=("Arial", 24, "bold"))
# lay out the component:
my_label.grid(column=0, row=0)
# my_label["text"] = "New text."
# # or
# my_label.config(text="New new text.")

# Button

def button_clicked():
    my_label["text"] = input.get()


button = Button()
button["text"] = "Click me!"
button["command"] = button_clicked
button.grid(column=1, row=1)

# Entry - input box

input = Entry(width=50)
input.grid(column=2, row=2)
#Add some text to begin with
input.insert(END, string="Some text to begin with.")
#Gets text in entry
print(input.get())
input.grid(column=4, row=2)

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.grid(column=3, row=3)

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(column=0, row=1)

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.grid(column=3, row=0)

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(column=3, row=1)

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=0, row=3)
radiobutton2.grid(column=0, row=3)


# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

# .pack() will "pack" widgets  one after another, default being center top, going down
# .place() will require an xy coordinates, so you need to work out exact, precise coordinate
# .grid() creates a grid of rows and cols, and it's related to other widgets
# you can change padding by using .config(padx=x, pady=y)

window.mainloop()
