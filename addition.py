while True:
    try:
        first = int(input("First number: "))
        second = int(input("Second number: "))
    except ValueError:
        print("You must enter a number!")
    else:
        print(first + second)