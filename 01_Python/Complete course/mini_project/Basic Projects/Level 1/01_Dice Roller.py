import random

def roll_dice():
    return random.randint(1, 6)

# Take player guess
guess = int(input("Guess the Dice roll number between 1-6: "))
print(f"Your guess is {guess}\n")

print("Rolling the Dice...")

while True:
    dice = roll_dice()
    print(f"Dice shows: {dice}")
    print("")

    if guess == dice:
        print("🎉 You Win!!!")
        break
    else:
        print("❌ Not a match.")

    if dice == 6:
        print("You rolled a 6! Rolling again...\n")
        continue   # roll again automatically
    else:
        print("Game Over! Better luck next time.")
        break
