while True:
    reason = input("Why do you like programming? ")
    if reason == 'quit':
        break
    with open("programming_poll.txt", 'a') as file_object:
        file_object.write(reason + "\n")