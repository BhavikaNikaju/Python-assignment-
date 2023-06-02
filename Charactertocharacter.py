Question11-python program to read character by character from a file

file_path = "path/to/your/file.txt"

file = open(file_path, "r")

character = file.read(1)

while character != "":

    print(character, end="")

    character = file.read(1)

file.close()

output :

This is the content of the file.

