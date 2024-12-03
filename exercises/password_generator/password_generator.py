import random

class PasswordGenerator(object):
    def __init__(self, passwordLen):
        self.passwordLen = passwordLen

    def determine(self):
        print("Determining password with Length : %s" % (self.passwordLen))
        charSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*())?"
        password = "".join(random.sample(charSet, self.passwordLen))
        print("Generated Password %s" % (password))
        print("--------------------------------------------")


if __name__ == "__main__":

    print("Entering Password Generator")
    passwordLen = int(input("Please enter the length you would like the password to be : "))
    print("Generating password with length %s" %(passwordLen))
    print("-------------------------------------------")

    generator = PasswordGenerator(passwordLen)
    generator.determine()