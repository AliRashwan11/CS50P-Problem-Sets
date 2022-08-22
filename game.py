import random
import sys

Level=input("Level:")

while not (Level.isdigit()):
    Level=input("Level:")
while not (int(Level)>0):
    Level=input("Level:")

Level=int(Level)

num=random.randint(1,Level)

while True:
    try:
        guess=int(input("Guess:"))
        break
    except ValueError:
        pass

while not(int(guess)==int(num)):
    if int(guess)>int(num):
        print("Too large!")
        while True:
            try:
                guess=int(input("Guess:"))
                break
            except ValueError:
                pass
    else:
        print("Too small!")
        while True:
            try:
                guess=int(input("Guess:"))
                break
            except ValueError:
                pass

print("Just right!")