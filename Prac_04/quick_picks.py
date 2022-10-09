import random

MINIMUM_PICK = 1
MAXIMUM_PICK = 45

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(0, number_of_quick_picks):
    line =""
    for i in range(0, 6):
        quick_pick = (random.randint(MINIMUM_PICK, MAXIMUM_PICK))
        quick_pick = str(quick_pick)
        line += (f"{quick_pick:>2} ")
    print(line)

