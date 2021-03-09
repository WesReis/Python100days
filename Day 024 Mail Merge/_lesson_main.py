# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# # Opening with the with command in read mode
# with open("my_file.txt", mode="r") as file:
#     contents = file.read()
#     print(contents)

# # opening in write mode, you can't read this file, but it will overwrite it
# # if you open a file in write mode it will create the file if it doesn't exist.
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

# Opening file in append mode, this will add to the end of the file.
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

#  Absolute file path /folder/folder/document (the first / means root)

# with open("/Users/leley/Desktop/new_file.txt") as file:
#     contents = file.read()
#     print(contents)

#  relative file path ./folder/document (./ means working directory)
# ../ means going backward one folder
# with open("../../../Users/leley/Desktop/new_file.txt") as file:
#     contents = file.read()
#     print(contents)
# not very good in this case

