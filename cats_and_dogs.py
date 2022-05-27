try:
    with open('cats.txt') as file_cat, open('dogs.txt') as file_dog:
        cats = file_cat.readlines()
        dogs = file_dog.readlines()
except FileNotFoundError:
    print("The file does not exist.")
    pass
else:
    for cat in cats:
        print(cat.rstrip().rstrip(','))
    for dog in dogs:
        print(dog.rstrip().rstrip(','))