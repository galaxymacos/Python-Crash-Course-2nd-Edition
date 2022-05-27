import json

filename = 'username.json'


def get_stored_username():
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    with open(filename, 'w') as f:
        username = input("What is your name? ")
        json.dump(username, f)

        return username


def greet_user():
    username = get_stored_username()
    answer = input(f"Is {username} your username? (y/n) ")
    if username and answer.lower() == 'y':
        print("Welcome back, ", username)
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
