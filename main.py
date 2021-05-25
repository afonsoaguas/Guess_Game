import random

def guess(min, max):
    random_number = random.randint(min, max)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between {min} and {max}: "))
        if guess < random_number:
            print("Too Low")
        elif guess > random_number:
            print("Too High")

    print("Congrats, the number was " + str(random_number)+".")


def computer_guess(Min, Max):
    feedback = ""
    guess = random.randint(Min, Max)
    while feedback != "c" :
        feedback = input(f"Is {guess} too high (h), too low (l) or correct (c): ")
        if feedback == "h":
            Max = guess - 1
            guess = random.randint(Min, Max)
        elif feedback == "l":
            Min = guess + 1
            guess = random.randint(Min, Max)

    print("I guess it, the number was: "+str(guess)+".")

print("Choose one of the option below: ")
print("- User Guess (u)")
print("- Computer Guess (c)")
print("")
choose = input("Option: ")

if choose == "u":
    print("Range of Numbers: ")
    Min = int(input("Min: "))
    Max = int(input("Max: "))
    guess(Min, Max)
elif choose == "c":
    print("Range of Numbers: ")
    Min = int(input("Min: "))
    Max = int(input("Max: "))
    computer_guess(Min, Max)
