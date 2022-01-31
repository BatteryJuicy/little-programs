import random


def import_food():
    food_options = []
    keep_going = True
    while keep_going:
        answer = input(
            "TO STOP ENTER: Y/N. Else, choose a food to add into the list: ")
        if answer.lower() == "n":
            keep_going = False
        else:
            food_options.append(answer)

    return food_options


def choose(arr):
    random_index = random.randint(0, len(arr) - 1)
    print(arr[random_index])


food_options = import_food()

choose(food_options)

input()