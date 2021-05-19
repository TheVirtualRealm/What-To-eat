import random

puerto_rican = ['Masa para pastelitos fritos', 'Pork and Beans with Rice', 'Pork Tacos', 'Quesadillas']
chin_ese = ['Sweet n Sour Chicken', 'Egg Rolls', 'Lo Mein', 'Fried Chicken and Rice']
ital_ian = ['Pizza', 'Fried Greens', 'Chicken Alfredo Pasta', 'creamy Beef Meat Pasta']
mexi_can = ['Chilaquiles', 'Burritos', 'Tamales', 'Elote']
dont_know = ['Dont Know']


def food_of_choice():
    place = input ("Where would you like to eat? ")
    if place == "Puerto Rican":
        print("Just a moment, ill find you the perfect meal.")
        print("I recomend: " +random.choice(puerto_rican))
    elif place == "Chinese":
        print("Just a moment, ill find you the perfect meal.")
        print("I recomend: " +random.choice(chin_ese))
    elif place == "Italian":
        print("Just a moment, ill find you the perfect meal.")
        print("I recomend: " +random.choice(ital_ian))
    elif place == "Mexican":
        print("Just a moment, ill find you the perfect meal.")
        print("I recomend: " +random.choice(mexi_can))
    else:
        print (input("thats fine, atleast we know who not to ask :D, please enter a number 1-4: "))
        random_choice = random.radient(1,4)
        if random_choice == 1:
            print("You Should eat: " +random_choice(puerto_rican))
        elif random_choice == 2:
            print("You Should eat: " +random_choice(chin_ese))
        elif random_choice == 3:
            print("You Should eat: " +random_choice(ital_ian))
        elif random_choice == 4:
            print("You Should eat: " +random_choice(mexi_can))
        else:
            print(" Please stop bothering me already ")
  

food_of_choice()