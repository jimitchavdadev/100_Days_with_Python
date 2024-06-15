# Open the file "my_file.txt" in read mode
# file = open("my_file.txt")

# Read the contents of the file into the variable "contents"
# contents = file.read()

# Print the contents of the file
# print(contents)

# Close the file
# file.close()

# Open the file "my_file.txt" in write mode using a context manager (with statement)
with open("my_file.txt", mode="w") as file:
    # Write the string "new text" to the file (this will clear all existing content)
    file.write("new text")
    
    # Write the string "\nmore text" to the file (this will append it to the existing content)
    file.write("\nmore text")

# In file modes:
# - 'w' stands for write mode (creates a new file or overwrites existing content)
# - 'r' stands for read mode
# - 'a' stands for append mode

# If a file does not exist and you open it in write mode ('w' or 'a'), it will be created.