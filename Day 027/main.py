import tkinter as tk

# Variables
window = tk.Tk()
# Custom title
window.title("My first GUI program.")
# size in pixels
window.minsize(width=500, height=300)

# Label
my_label = tk.Label(text="I am a label.", font=("Arial", 24, "bold"))
# lay out the component:
my_label.pack(side="left")
# Default arguments don't need to be modified

# Unlimited arguments - *args
# def function(*args):
#     for n in args:
#         print(n)
# *args will be seen as a tuple, with any number of inputs
# import playground
# print(playground.add(10,22,35,46))

# Keyword unlimited args - **kwargs (where kwargs = dictionary






window.mainloop()
