# if you have 3 lives. I roll the dice. If i roll 6, you win
# if not a 6, you lose 1 life.

from random import randint

lives=3
while lives > 0:
    roll=randint(1,6)# make sure to not put a: and b:
    if roll==6:
        print("You rolled a 6, You win")
        break# this exists the while even if lives still> 0
    else:
        print(f"you rolled a {roll}! You lose a life")
        lives-=1
        print(f" lives left: {lives}")

if lives==0:
    print("You lost")
    