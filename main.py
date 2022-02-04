import random

CPUGuessedInt = random.randint(1, 49)

print(CPUGuessedInt)

HUMANGuessedInt = input("Guess a number from 1 to 49" )
int(HUMANGuessedInt)

if int(HUMANGuessedInt) > CPUGuessedInt:
    print("Your guess is too high")

elif int(HUMANGuessedInt) < CPUGuessedInt:
    print("Your guess is too low")

elif int(HUMANGuessedInt) == CPUGuessedInt:
    print("you are correct!")