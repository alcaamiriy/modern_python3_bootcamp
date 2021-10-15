
import random


random_number = random.randint(1, 10)
keep_playing = True
msg = "Guess a number between 1 - 10: "
correct_msg = "YEEEY!, You guest it CORRECTLY! Do you want keep playing? y/n: "
guested_number = int(input(msg))

while keep_playing:
    if guested_number == random_number:
        response = input(correct_msg)
        if response.lower().startswith("y"):
            guested_number = int(input(msg))
            random_number = random.randint(1, 10)
        elif response.lower().startswith("n"):
            print("Bye! Thanks for playing.")
            break
        else:
            response = input(correct_msg)
    if guested_number < random_number:
        guested_number = int(input(
            f"{guested_number} is TOO LOW, try again: "
        ))
    else:
        guested_number = int(input(
            f"{guested_number} is TOO HIGH, try again: "
        ))
