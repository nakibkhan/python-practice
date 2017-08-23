
class CowsAndBullsDeterminator(object):
    def __init__(self, randomGeneratedNumber, userGuessedNumber):
        self.randomGeneratedNumber = randomGeneratedNumber
        self.userGuessedNumber = userGuessedNumber

    def determine(self):
        print 'Random Number Generated : %s' %(self.userGuessedNumber)
        print 'User Generated Number   : %s' %(self.randomGeneratedNumber)

        list_guess = [int(i) for i in str(self.userGuessedNumber)]
        list_random = [int(i) for i in str(self.randomGeneratedNumber)]

        cows = 0
        bulls = 0

        for x,y in zip(list_guess, list_random):
            print zip(list_guess, list_random)
            if(x==y):
                ++cows

