guest_name = input("Guest name: ")
with open("guest.txt", 'w') as file_object:
    file_object.write(guest_name)
