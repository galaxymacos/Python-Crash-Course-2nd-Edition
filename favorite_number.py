import json


def write_fav_number():
    try:
        fav_number = int(input("Fav number: "))
    except ValueError:
        print("Please enter a number.")
    else:
        with open("fav_number.json", "w") as f:
            json.dump(fav_number, f)
            print("Saved!")


def read_fav_number():
    try:
        with open("fav_number.json", "r") as f:
            fav_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_number


if read_fav_number():
    print("I know your fav number! It's " + str(read_fav_number()))
else:
    write_fav_number()