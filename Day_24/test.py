# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("my_file.txt", mode="w") as file:
    file.write("new text")
    # this will clear all the content and add the string
    file.write("\nmore text")
    # this will append it

# w for write, r for read and a for append
# if a file does not exist in write mode, it will create a file
