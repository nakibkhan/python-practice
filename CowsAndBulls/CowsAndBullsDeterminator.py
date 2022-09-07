class CowsAndBullsDeterminator(object):
    def __init__(self, randomGeneratedNumber, userGuessedNumber):
        self.randomGeneratedNumber = randomGeneratedNumber
        self.userGuessedNumber = userGuessedNumber

    def determine(self):
        print('Random Number Generated : %s' % self.userGuessedNumber)
        print('User Generated Number   : %s' % self.randomGeneratedNumber)

        list_guess = [int(i) for i in str(self.userGuessedNumber)]
        list_random = [int(i) for i in str(self.randomGeneratedNumber)]

        cows = 0
        bulls = 0

        print(list(zip(list_guess, list_random)))
        for x, y in zip(list_guess, list_random):
            if x == y:
                cows += 1

        print('---------------------------------------')
        print('There are %s Cow(s)' % (cows))
        print('---------------------------------------')

        i = 0
        while i < len(list_guess):
            if (list_guess[i] in list_random) and (list_random.index(list_guess[i]) != i):
                bulls += 1
            i += 1

        print('There are %s Bull(s)' % (bulls))
        print('---------------------------------------')
