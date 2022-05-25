messages = ["I", "Love", "Python"]


def show_messages(texts):
    sent_messages = []
    while len(texts) > 0:
        message = texts.pop()
        print(message)
        sent_messages.append(message)


print("Original messages", messages)
show_messages(messages[:])
print("After messages", messages)