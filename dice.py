import random

min = 1
max = 6

enterDice = int(input("Number of dices : "))
uinput = "y"

while uinput == "y":
    for x in range(enterDice):
        print(random.randint(min, max))
    uinput = input("Again? [y/n]  : ")
