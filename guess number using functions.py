import random

def guess_number():
    global guess
    for i in range(1, 5):
        print("try to guess the number")
        guess = int(input("try to put the correct number:"))

        if guess > secretNumber:
            print("no bother,number u choosed is too high !!!")
        elif guess < secretNumber:
            print("nope the number you choosed is lower")

        else:
            break
    return guess

def checker(guess,secretNumber):
    if guess == secretNumber:
        print("yessss you did it ,greattt!!!!,congoooo!!!!!!")
    else:
        print("the correct number is" + str(secretNumber))

secretNumber=random.randint(1,30)
print("you should think about the number")

guess=guess_number()
checker(guess,secretNumber)

