try:
    with open("alice.txt", encoding='utf-8') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("The file alice.txt does not exist.")
else:
    print(len(contents.split()))