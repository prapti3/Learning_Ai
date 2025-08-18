import random

# 2. Number Guessing Game
#    - Computer generates a random number.
#    - User keeps guessing until correct, with hints ("Too high / Too low").


# take input number
# check if user input matches the random number generated


print("Let's Guess the number")

Guess_num = int(input("Guess the number between 1 to 20:- "))
Random_num = random.randint(1, 20)


if Guess_num == Random_num:
    print("Yoooo!!!, You win")

elif Guess_num > Random_num:
    print("Too high")
elif Guess_num < Random_num:
    print("Too Low")

elif Guess_num != Random_num:
    print("Better Luck next time ")

print(f"Your Guessed number is {Guess_num} and Expected number is {Random_num}")



