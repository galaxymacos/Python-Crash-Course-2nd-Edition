def count_word(filename):
    try:
        with open(filename, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print("The file " + filename + " does not exist.")
        # can use pass to fail silently
    else:
        return len(text.split())


print(count_word("alice.txt"))
