import random

print("Hello and welcome to the guess the capital game")
print("You will be given a country and 5 cities")
print("Four cities are not capitals, and one is a capital.\n")

    
def read_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    chosen_lines = []

    for line in lines:
        chosen_lines.append(line.strip())

    return chosen_lines


non_capitals = read_file("non_capital_cities.txt")
capitals = read_file("capital_cities.txt")

print(capitals)

def decide_which_cities():

    # decide capital and its country
    print("Capitals:", capitals)
    print("Number of capitals:", len(capitals)) 
    capital_info = random.choice(capitals)
    one_capital, country = capital_info.split(",")

    # Choose four non-capital cities
    four_cities = []

    for i in range(4):
        city = random.choice(non_capitals)

        while city in four_cities:
            city = random.choice(non_capitals)

        four_cities.append(city)

    all_cities = four_cities + [one_capital]

    random.shuffle(all_cities)

    print("\nWhich one of these is the capital of", country, "?")

    for city in all_cities:
        print(city)

    answer = input("Your answer: ")

    if answer.strip().lower() == one_capital.strip().lower():
        print("Correct! Well done!")
    else:
        print("Not quite! The correct answer is", one_capital)


decide_which_cities()


