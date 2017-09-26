import random
from CowsAndBulls.CowsAndBullsDeterminator import CowsAndBullsDeterminator

if __name__ == "__main__":
    print "Entering Cows and Bulls Game !!!!!"
    print '------------------------------------------'

    userGuessNumber = 0

    while(len(str(userGuessNumber)) < 4):
        userGuessNumber = int(input("Please Enter is a 4 Digit Number "))

    cowsAndBullsDeterminator = CowsAndBullsDeterminator(userGuessNumber, random.randint(1000,9999))
    cowsAndBullsDeterminator.determine()
