try:
    with open("pride and prejudice.txt") as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("The file does not exist.")
else:
    print(contents.lower().count("me"))
