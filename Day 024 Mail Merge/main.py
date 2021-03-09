# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
#
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    for name in names:
        new_name = name.strip("\n")

        with open("./Input/Letters/starting_letter.txt") as template:
            letter_contents = template.read()
            new_letter = letter_contents.replace(PLACEHOLDER, new_name)

        filename = f"letter_for_{new_name}.txt"
        with open("./Output/ReadyToSend/"+filename, mode="w") as letter:
            letter.write(new_letter)
