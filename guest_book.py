while True:
    guest_name = input("Guest name: ")
    print("Greetings, " + guest_name.title() + "!")
    with open("guest_book.txt", 'a') as file_object:
        file_object.write(guest_name + "\n")