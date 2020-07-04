import os
import random

MONTHS = [
    ("Jan", 31),
    ("Feb", 29),
    ("Mar", 31),
    ("Apr", 30),
    ("May", 31),
    ("Jun", 30)
    # ("Jul", 31),
    # ("Aug", 31),
    # ("Sep", 30),
    # ("Oct", 31),
    # ("Nov", 30),
    # ("Dec", 31)
]

MAX_COMMITS = 15
MANY_ZEROS = 10

randoms = []
for zero in range(1, MANY_ZEROS+1):
    randoms.append(0)
randoms += [x for x in range(1,MAX_COMMITS+1)]


def switch_state(state: str):
    if state == "0":
        state = "1"
    else:
        state = "0"
    return state

def main():
    state = "0"
    for month in MONTHS:
        for day in range(1, month[1]+1):
            random_number = random.choice(randoms)
            for times in range(1, random_number):
                os.system(f"echo {state} > test")
                os.system("git add test")
                os.system("git commit --allow-empty-message -m 'oof'")
                command = "git commit --amend --no-edit --date " + '"' + str(day) + " " + str(month[0]) + " " + str(day) + " " + "22:22:22 2020 +0200" + '"'
                os.system(command)
                state = switch_state(state)


main()
